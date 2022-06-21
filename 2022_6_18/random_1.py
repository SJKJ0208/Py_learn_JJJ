# import matplotlib.pyplot as plt
# from random import choice
# import pygal
# class RandomWalk():
#     """一个生成随机漫步的属性"""
#     def __init__(self,num_points = 10000):
#         """初始化"""
#         self.num_points = num_points
#
#         #漫步始于（0,0）
#         self.x = [0]
#         self.y = [0]
#
#     def fill_walk(self):
#         """计算所有的点"""
#         while len(self.x) < self.num_points:
#             x_direction = choice([1,-1])
#             x_distance = choice([0,1,2,3,4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1,-1])
#             y_distance = choice([0,1,2,3,4])
#             y_step = y_direction * y_distance
#
#             #拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             #计算下一个点的位置_使用上次最后一个数据进行新的计算
#             next_x = self.x[-1]+x_step
#             next_y = self.y[-1]+y_step
#
#             self.x.append(next_x)
#             self.y.append(next_y)
#
# rw = RandomWalk()
# rw.fill_walk()
# gal = pygal.Bar()
# gal.title("random walk")
# gal.x_title("x_position")
# gal.x_labels('')
# gal.y_title("y_position")
#
# gal.add('random',)







