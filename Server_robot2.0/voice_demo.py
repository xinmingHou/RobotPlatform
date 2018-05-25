#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: voice_demo.py
@time: 2018/5/16 下午1:46
@description:
'''

from api.AipSpeech.VoiceController import *

dashgo_serialname = "/dev/tty.wchusbserial1440"

controler = voiceController(configs_path="configs.yaml",
                            dashgo_serialname=dashgo_serialname)

