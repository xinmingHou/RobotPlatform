#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: SpeechPlayer.py
@time: 2018/5/14 下午5:59
@description:
    初始化播放器
    使用播放器的播放命令时输入路径
        判断文件是否存在
            存在就播放
            不存在就退出

'''
import pyaudio
import wave
import yaml
import os
import matplotlib.pyplot as plt
import numpy as np


class speechPlayer:
    def __init__(self, chunk=1024):
        self.chunk = chunk


    def play(self, filepath):
        if not os.path.exists(filepath):
            print("文件不存在")
            exit()

        #     播放录音     #
        print("**播放%s**" % filepath)
        wf = wave.open(filepath, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(self.chunk)
        # data是二进制的数据，所以这里是二进制的空数据
        while data != b'':
            stream.write(data)
            data = wf.readframes(self.chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()

    # 这个功能没有写好，是用波形图展示命令，没什么实际用途
    def show_wave(self):
        f = wave.open(self.WAVE_OUTPUT_FILENAME, 'rb')
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]

        strData = f.readframes(nframes)  # 读取音频，字符串格式
        waveData = np.fromstring(strData, dtype=np.int16)  # 将字符串转化为int
        waveData = waveData * 1.0 / (max(abs(waveData)))  # wave幅值归一化
        # plot the wave
        time = np.arange(0, nframes) * (1.0 / framerate)
        plt.plot(time, waveData)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude")
        plt.title("Single channel wavedata")
        plt.grid('on')  # 标尺，on：有，off:无。


if __name__ == '__main__':
    configs = yaml.load(open('../configs.yaml'))

    # 在播放文件时，chunk是数据流的大小，设置成多少都可以。这里为保持严谨性，设置与录制时相同。
    player = speechPlayer(configs["device_para"]["CHUNK"])

    # player = speechPlayer(2000)

    player.play(configs["wave_output_filename"])
