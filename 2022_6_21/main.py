import csv
filename = 'test.csv'
with open(filename,encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    header_row = next(reader)
    # print(header_row)

    higts = []
    for row in reader:
        higts.append(int((row[0])))
    print(higts)
    for index,value in enumerate(header_row):
        print(index,value)

from matplotlib import pyplot as plt
import numpy as np
filename = 'test2.csv'
with open(filename,encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    higts = []
    index = []
    places = []
    for value in reader:
        higts.append(int(value[2]))
        index.append(int(value[0]))
        places.append(str(value[1]))
    print(header_row[2])
    print(higts)
    print(index)
index = np.arange(len(places))
fig = plt.figure(figsize=(15,6))
plt.plot(places,higts,c='red')
title = str(header_row[2])
#设置字体为楷体
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.title(title,fontsize=24)
# 显示中文或者一些需要对应的文本，需要一个index序列进行对应
# plt.xticks(index,places)
plt.xlabel("Places",fontsize=5)
plt.ylabel("Tem——Hight",fontsize=24)
# 调用方法再放入主体
plt.Figure.autofmt_xdate(fig)
plt.tick_params(axis='both',which='major',labelsize=8)
# which的值为 'major'、'minor'、'both'，分别代表设置主刻度线、副刻度线以及同时设置
# path https://www.jianshu.com/p/0fdf6c003c80 can see the params


plt.show()
