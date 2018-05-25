#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: REC.py
@time: 2018/5/15
@description:
    录音机
    输入录音设备本身的参数，
    需要存储成的音频文件的参数

'''

import pyaudio
import wave
import numpy as np


class recorder:
    def __init__(self, device_para, aipSpeech_wav_para):
        self.device = device_para
        self.target_wav_para = aipSpeech_wav_para

    def record(self, wave_output_filename, record_seconds=2):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.device['FORMAT'],
                        channels=self.device["CHANNELS"],
                        rate=self.device["RATE"],
                        input=True,
                        frames_per_buffer=self.device["CHUNK"])

        print("* recording")

        frames = []

        for i in range(0, int(self.device["RATE"] / self.device["CHUNK"] * record_seconds)):
            data = stream.read(self.device["CHUNK"])
            frames.append(data)

        print("* done recording")
        print("* saving wave file")
        stream.stop_stream()
        stream.close()
        p.terminate()

        frames = b''.join(frames)
        audio_data_short = np.fromstring(frames, np.short)

        if self.device["CHANNELS"] > 1:
            audio_data_short = audio_data_short[::self.device["CHANNELS"]]

        # resample设备录音到符合API条件的录音文件
        tar_rate = np.int(self.target_wav_para["RATE"])

        audio_data_short0 = self.Resample(audio_data_short, self.device["RATE"], tar_rate)

        wf = wave.open(wave_output_filename, 'wb')

        wf.setnchannels(self.target_wav_para["CHANNELS"])
        wf.setsampwidth(self.target_wav_para["SAMPWIDTH"])
        wf.setframerate(self.target_wav_para["RATE"])
        wf.writeframesraw(audio_data_short0)
        wf.close()
        print("* saving done")

    def Resample(self, input_signal, src_fs, tar_fs):
        '''

        :param input_signal:输入信号
        :param src_fs:输入信号采样率
        :param tar_fs:输出信号采样率
        :return:输出信号
        '''

        dtype = input_signal.dtype
        audio_len = len(input_signal)
        audio_time_max = 1.0 * (audio_len - 1) / src_fs
        src_time = 1.0 * np.linspace(0, audio_len, audio_len) / src_fs
        tar_time = 1.0 * np.linspace(0, np.int(audio_time_max * tar_fs), np.int(audio_time_max * tar_fs)) / tar_fs
        output_signal = np.interp(tar_time, src_time, input_signal).astype(dtype)

        return output_signal




if __name__ == '__main__':
    import yaml
    configs = yaml.load(open('../configs.yaml'))
    # 声明一个录音机，输入录音设备的参数，以及需要转换成的参数
    rec = recorder(configs["device_para"], configs["aipSpeech_wav_para"])
    # 录多少秒,默认2秒
    # 第二个是路径
    rec.record(configs["RECORD_SECONDS"], configs["wave_output_filename"])








