#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: NLP.py
@time: 2018/3/28 下午8:35
@description:
    这是个翻译器
'''

from aip import AipSpeech
class NLP:
    def __init__(self, app_token, aipSpeech_wav_para):
        self.app_token = app_token
        self.target_wav_para = aipSpeech_wav_para

        self.client = AipSpeech(self.app_token["APP_ID"], self.app_token["API_KEY"], self.app_token["SECRET_KEY"])

    # 读取文件
    def get_file_content(self, file_path):
        print("* get wave file")
        with open(file_path, 'rb') as fp:
            return fp.read()
        # 识别本地文件

    def translate(self, file_path):
        print("* start translate")
        result = self.client.asr(self.get_file_content(file_path), self.target_wav_para["SPEECH_FILE_STYLE"],
                                 self.target_wav_para["RATE"], {'dev_pid': self.target_wav_para["dev_pid"],})
        print("* done translate")
        return result

    def result(self, file_path):
        result = self.translate(file_path)
        if result['err_no'] == 0:
            return result['err_no'], result['result'][0]
        else:
            print(result['err_msg'])
            return result['err_no'], result['err_msg']


if __name__ == '__main__':
    import yaml
    configs = yaml.load(open('../configs.yaml'))
    # filepath = "../tempFile/20180404103639.wav"

    # 声明翻译器
    nlp = NLP(configs["baidu_token"], configs["aipSpeech_wav_para"])

    # 翻译
    # result = nlp.translate(configs["wave_output_filename"])['result']
    # print(result[0])

    err_no, result = nlp.result(configs["wave_output_filename"])
    print(err_no, result)
