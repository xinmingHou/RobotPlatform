#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: robot_parament.py
@time: 2018/3/26 下午6:45
@description:
'''



# 600~2400代表0~180

armNum = {"L1": '0D', "L2": '0E',"L3": '0F', "L4": '18', "L5": '19', "L6": '1A',
          "R1": '0C', "R2": '0B', "R3": '0A', "R4": '07', "R5": '06', "R6": '05'}
fingerNum = {"L1": '1F', "L2": '1E',"L3": '1D', "L4": '1C', "L5": '1B',
            "R1": '00', "R2": '01', "R3": '02', "R4": '03', "R5": '04'}

armDefault = {"L1": 40, "L2": 140, "L3": 90, "L4": 140, "L5": 90, "L6": 90,
          "R1": 140, "R2": 40, "R3": 90, "R4": 40, "R5": 90, "R6": 90}

fingerDefault = {"L1": 140, "L2": 140, "L3": 140, "L4": 40, "L5": 40,
            "R1": 40, "R2": 40, "R3": 40, "R4": 140, "R5": 140}

#全部都有位姿的，按照左臂，左手，右臂、右手顺序调整
allmove_seq=['0D', '0E', '0F', '18', '19', '1A', '1F', '1E', '1D', '1C', '1B',
             '0C', '0B', '0A', '07', '06', '05', '00', '01', '02', '03', '04']

defaultAction = {'0D': 40, '0E': 140, '0F': 90, '18': 140, '19': 90, '1A': 90,
                 '1F': 140, '1E': 140, '1D': 140, '1C': 40, '1B': 40,
                '0C': 140, '0B': 40, '0A': 90, '07': 40, '06': 90, '05': 90,
                 '00': 40, '01': 40, '02': 40, '03': 140, '04': 140}



# 5555470316D00707E80306DC0505DC050CD0070BE8030ADC051ADC0518D00719DC050ED0070FDC050DE80303D00704D0071CE8031BE8031ED0071DD00701E8031FD00702E80300E803

reset_cmd = "5555470316D00707E80306DC0505DC050CD0070BE8030ADC051ADC0518D00719DC050ED0070FDC050DE80303D00704D0071CE8031BE8031ED0071DD00701E8031FD00702E80300E803"




# 加一个angle必须要在一位小数的约束。0.3度的控制
def angle2pwm(angle):
    pwm = angle * 10 + 600
    return pwm

# 角度转成16进制命令
def angle2cmd_hex(angle):
    return cmd2cmd_hex(angle2pwm(angle))

# 数转成16进制命令
def number2cmd_hex(number):
    if number < 16:
        return "0"+str(hex(number))[2:3].upper()
    else:
        return str(hex(number))[2:].upper()

# 命令转成16进制命令
def cmd2cmd_hex(number):
    tempstr = str(hex(number)[2:]).upper().zfill(4)  # 用0补齐4位
    low_eight = tempstr[2:]
    high_eight = tempstr[:2]
    return low_eight, high_eight




