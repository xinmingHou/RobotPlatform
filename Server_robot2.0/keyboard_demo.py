#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: keyboard_demo.py
@time: 2018/3/26 下午7:14
@description:
'''

from api.keyboard_controler import *

robot_serialname = "/dev/tty.wchusbserial1460"
dashgo_serialname = "/dev/tty.wchusbserial1440"



app = QApplication(sys.argv)
controler = keyboard_controler(robot_serialname=robot_serialname, dashgo_serialname=dashgo_serialname)
sys.exit(app.exec_())