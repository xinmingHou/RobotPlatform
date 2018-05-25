#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: dashgo_interface.py
@time: 2018/3/26 下午6:48
@description:
'''

# coding:utf-8
from .dashgo_parament import *
import serial
#import serial.tools.list_ports

## ls /dev/tty.*


class dashgo:
    def __init__(self, serial_name, boutrate=115200, timeout=2, safe_distance=5):
        self.serial_name = serial_name
        self.boutrate = boutrate
        self.timeout = timeout
        self.safe_distance = safe_distance
        self.ser = self.__openserial__()
        self.reset()



    # 打开端口
    def __openserial__(self):
        ser = serial.Serial(self.serial_name, self.boutrate, timeout=self.timeout)
        print("check which port was really used >", ser.name)

        print("open serial")
        if ser.is_open:
            print("serial is open")
        else:
            print("serial not open")
            exit(0)
        return ser


    # 初始化参数，主要是把两轮的里程清零
    def reset(self):
        self.ser.write("r\r".encode(encoding="utf-8"))
        answer = self.ser.readline()
        print("length be reset %s" % answer)


    # 原始命令控制
    def ori_run(self, l, r):
        if l > MaxVindoor or l < -MaxVindoor or r > MaxVindoor or r < -MaxVindoor:
            print("So Fast!")
        else:
            tempcmd = "z %d %d\r" % (l, r)
            self.ser.write(tempcmd.encode(encoding="utf-8"))


    # 自定义控制，输入两轮速度
    def robot_run(self, vleft=0.10, vright=0.10):
        vl = v_paramater(vleft)
        vr = v_paramater(vright)
        self.ori_run(vl, vr)


    # 直走，可以设定运行速度（m/s）
    def go_forward(self, direction=True, velocity=0.1):
        if not direction:
            velocity=-velocity
        self.robot_run(velocity, velocity)


    # 转向，默认顺时针转
    #direction=True ,右转
    # 可以调整转弯角度(rad)，角速度(rad/s)，角速度为正数 表示右转，负数表示左转
    # 默认角速度(Pi/4)/s，
    def turn(self, direction=True, angular_velocity=Pi/4):
        vl, vr = r_paramater(angular_velocity)
        if not direction:
            vl = -vl
            vr = -vr
        self.robot_run(vl, vr)
    # 停车
    def stop(self):
        self.robot_run(0, 0)


    # 轮子转动过的总长度，左右轮可能不一样
    def get_length(self):
        self.ser.write("e\r".encode(encoding="utf-8"))
        answer = self.ser.readline()
        l, r = list(map(eval, answer.split()))
        l_wheel_length = l/ticks_per_meter
        r_wheel_length = r/ticks_per_meter
        print("the left wheel  %f m, the right wheel  %f m" % (l_wheel_length, r_wheel_length))
        return l_wheel_length, r_wheel_length

    # 返回雷达距离,单位厘米0
    def collision_detect(self):
        self.ser.write("p\r".encode(encoding="utf-8"))
        answer = self.ser.readline()
        # left, front, right, rear = list(map(eval, answer.split()))
        # return left, front, right, rear
        return answer

    #############################################################################
    #                         功能函数
    #############################################################################

    # 简单碰撞检测： 前进方向遇到障碍， 小于安全距离则向右转一定角度再检测，知道三个数值都大于安全距离，则继续前进
    def obstacle_avoid(self):
        pass












