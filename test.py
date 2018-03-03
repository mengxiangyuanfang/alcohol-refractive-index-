import numpy as np
import math
import matplotlib.pyplot as plt
import pandas
from decimal import *

list1 =[]
for i in np.arange(-5, 35, 0.001):
    list1.append(i)
delta_T = np.array([list1]).T
# print(delta_T.shape)
RefIndex = 1.369290000000000 - 0.00040010000000*delta_T
# print(RefIndex.shape)
list2 = []
# print(len(RefIndex)-1)
for i in range(len(RefIndex)-1):
    a = RefIndex[i + 1,0] - RefIndex[i,0]
    list2.append(a)
delta_RefIndex = np.array([list2]).T

length = 1
Lambda = 1550*pow(10, -9)
delta_angle = (2*math.pi*delta_RefIndex*length/Lambda)
intensity_list = [math.cos(x) for x in delta_angle]
intensity = np.array([intensity_list]).T

list3 =[]
for i in range(len(intensity)-1):
    list3.append(intensity[i+1,0]-intensity[i,0])
delta_intensity = np.array([list3]).T

# plt.scatter(delta_RefIndex, 2*math.pi*delta_RefIndex*length/Lambda)
#
# plt.show()
# print(delta_RefIndex[111])
# print(delta_angle[111])


# print(delta_T.shape)
# print(RefIndex.shape)
# print(delta_RefIndex.shape)
# print(delta_angle.shape)
# print(delta_intensity.shape)


print(delta_T.min())
print(RefIndex.min())
print(delta_RefIndex.min())
print(delta_angle.min())
print(delta_intensity.min())


# d = np.vstack((delta_T[0:39998,0],RefIndex[0:39998,0],delta_RefIndex[0:39998,0],delta_angle[0:39998,0],delta_intensity[0:39998,0])).T
# print(d.shape)
#
# data1 = pandas.DataFrame(d)
# data1.to_csv('data1.csv')
