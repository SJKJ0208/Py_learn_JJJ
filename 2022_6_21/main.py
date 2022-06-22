# import csv
# filename = 'test.csv'
# with open(filename,encoding='utf-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     header_row = next(reader)
#     # print(header_row)
#
#     higts = []
#     for row in reader:
#         higts.append(int((row[0])))
#     print(higts)
#     for index,value in enumerate(header_row):
#         print(index,value)
#
# from matplotlib import pyplot as plt
# import numpy as np
# filename = 'test2.csv'
# with open(filename,encoding='utf-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     higts = []
#     index = []
#     places = []
#     for value in reader:
#         higts.append(int(value[2]))
#         index.append(int(value[0]))
#         places.append(str(value[1]))
#     print(header_row[2])
#     print(higts)
#     print(index)
# index = np.arange(len(places))
# fig = plt.figure(figsize=(15,6))
# plt.plot(places,higts,c='red')
# title = str(header_row[2])
# #设置字体为楷体
# plt.rcParams['font.sans-serif'] = ['KaiTi']
# plt.title(title,fontsize=24)
# # 显示中文或者一些需要对应的文本，需要一个index序列进行对应
# # plt.xticks(index,places)
# plt.xlabel("Places",fontsize=5)
# plt.ylabel("Tem——Hight",fontsize=24)
# # 调用方法再放入主体
# plt.Figure.autofmt_xdate(fig)
# plt.tick_params(axis='both',which='major',labelsize=8)
# # which的值为 'major'、'minor'、'both'，分别代表设置主刻度线、副刻度线以及同时设置
# # path https://www.jianshu.com/p/0fdf6c003c80 can see the params
# plt.show()

import json

#将数据加载到一个列表中
import pygal
import math

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
dates = []
months = []
weeks = []
weekdays = []
closes = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))
for i in range(len(dates)):
    print("{} is month {} week {},{},the close price is {}RMB".format(dates[i],months[i],weeks[i],weekdays[i],closes[i]))

# from matplotlib import pyplot as plt
# fig = plt.figure(figsize=(20,10))
# plt.title('close RMB')
# plt.plot(dates,closes)
# plt.Figure.autofmt_xdate(fig)
# plt.show()

import pygal as gal
line_chart = pygal.Line(x_label_rotation =20,show_minor_x_labels = False)
line_chart.title = '收盘价￥'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]
line_chart.add('收盘价log',closes_log)
line_chart.render_to_file('收盘价折线图（￥）log.svg')
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价.svg')

from itertools import groupby

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []

    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _,v in y ]
        xy_map.append([x,sum(y_list) / len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
print(idx_month)
#相当于到idx_month这个地方停下
# draw_line(months[:idx_month],closes[:idx_month],'收盘价月均值(￥)','月日均值')

idx_month = dates.index('2017-12-11')
draw_line(weeks[1:idx_month],closes[1:idx_month],'收盘价月均值(￥)','月均值')

#整合表格
with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
        '收盘价.svg',
        '收盘价月均值(￥).svg'
        '收盘价折线图（￥）.svg'
        '收盘价折线图（￥）log.svg'
    ]:
        html_file.write('   <object type = "image/svg+xml" data = "{0}" height =500></object>\n'.format(svg))
        html_file.write('</body></html>')