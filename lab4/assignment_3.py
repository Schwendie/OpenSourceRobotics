import numpy as np
import matplotlib.pyplot as plt

from math import atan2, sqrt

dt = 0.01
alpha = 0.98

roll_angle, pitch_angle = 0, 0
values = []
roll_rate = []
pitch_rate = []
roll = []
pitch = []
roll_angle_list = []
pitch_angle_list = []
val = []

plt.ion()

with open("raw_imu_data.txt", "r") as file:
    for line in file:
        data = line.rstrip().split(' ')
        data[5] = float(data[5]) # gyro_z
        data[4] = float(data[4]) # gyro_y
        data[3] = float(data[3]) # gyro_x
        data[2] = float(data[2]) # acc_z
        data[1] = float(data[1]) # acc_y
        data[0] = float(data[0]) # acc_x
        values.append(data)

for point in values:
    roll.append(atan2(point[1], point[2]))
    pitch.append(atan2(-point[0], sqrt(point[2]**2 + point[1]**2)))
    roll_rate.append(point[3])
    pitch_rate.append(point[4])

for i in range(0, 891):
    roll_angle = alpha * (roll_angle + roll_rate[i] * dt) + (1 - alpha) * roll[i]
    pitch_angle = alpha * (pitch_angle + pitch_rate[i] * dt) + (1 - alpha) * pitch[i]
    roll_angle_list.append(roll_angle)
    pitch_angle_list.append(pitch_angle)
    val.append(i * dt)

for i in range(len(roll_angle_list)):
    plt.cla()
    plt.plot(val[:i], roll_angle_list[:i], 'r--')
    plt.plot(val[:i], pitch_angle_list[:i], 'b--')
    plt.show()
    plt.pause(0.001)
