#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: dashgo_parament.py
@time: 2018/3/26 下午6:45
@description:
'''


# dashgo_D1 的基本参数
wheel_diameter = 0.1260       # 轮子直径,单位:米
wheel_track = 0.3500          # 两个轮子的间距,单位:米
encoder_resolution = 1200.0000     # 编码器分辨率,轮子转一圈，编码器产生的脉冲数
PID_RATE = 30.0000                 # PID 调节 PWM 值的频率
Pi = 3.1415926                  # 算周长的pi

MaxV = 80
MaxVindoor = 50

# 每移动 1 米产生脉冲信号
ticks_per_meter = encoder_resolution / (wheel_diameter * Pi)

# 指令z 20 -20  表示左轮20的速度向前。右轮20的速度向后。
# （实际运动就是顺时针自转）


# 只有线速度
# v表示速度，单位是m/s，order_v返回的是该速度换算出的指令的数值
def v_paramater(v):
    return int(v * ticks_per_meter / PID_RATE)


# 只有角速度
# 自转，就需要一个轮子正转，一个轮子反转,转速相同  （z 19 -19 表示顺时针转）
# r表示角速度，单位是rad/s，r > 0 ,vl表示左轮，vr是右轮
def r_paramater(r):   # >0顺时针
    # 转换成两个轮子的线速度
    vl = r * wheel_track / 2.0
    vr = -1 * r * wheel_track / 2.0

    # 算出参数
    return vl, vr


# 既有角速度V1，又有线速度V2
def v_r_paramater(v1, v2):
    vl = v2 + v1 * wheel_track / 2.0
    vr = v2 - v1 * wheel_track / 2.0
    # 算出参数
    return vl, vr







