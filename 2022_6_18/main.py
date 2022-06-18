# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#learn impact new mode
import pylab as pl

import pizza
pizza.make_pizza(16,'ssss','dddd','yyy')


from pizza import make_pizza
make_pizza(16,'ssss','dddd','yyy')

#give a name to function
from pizza import make_pizza as mp
mp(16,'ssss','dddd','yyy')

#give a name for mode
import pizza as p
p.make_pizza(16,'ssss','dddd','yyy')

#import all function in the mode
from pizza import *
make_pizza(16,'ssss','dddd','yyy')
#we should not use it


#Class
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化小狗的属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over")

#use the class of dog
my_dog = Dog('Hwm',20)

print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()

class Restaurant():
    """餐馆"""
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.num = 0

    def describe(self):
        print(self.name)
        print(self.type)

    def open(self):
        print("open")

    def modify_name(self,name):
        self.name = name

    def set_num(self,num):
        self.num = num
        print(self.num)

    def increment_num(self):
        self.num+=1


restaurant = Restaurant('hhh','china')
restaurant.describe()
restaurant.open()

#we can modify the class' variables

#we can modidiy by exactly
restaurant.name = 'ttt'
restaurant.describe()
restaurant.modify_name('lll')
restaurant.describe()


#9-4
dian = Restaurant('yui','china')
dian.increment_num()
dian.increment_num()
dian.increment_num()
dian.increment_num()
print(dian.num)

#9-5
class User():
    """尝试登陆"""
    def __init__(self):
        self.login_attempts = 0

    def increase_login_attempts(self):
        self.login_attempts+=1

    def reset_attempts(self):
        self.login_attempts = 0

user = User()
user.increase_login_attempts()
user.increase_login_attempts()
user.increase_login_attempts()
print(user.login_attempts)
user.reset_attempts()
print(user.login_attempts)

#inherit
class Black_res(Restaurant):
    """黑心饭店"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        #the second init is below for father
        super(Black_res, self).__init__(make,model)
        self.pay = 50000
        self.year = year
        self.type = model


    def prin_we_pay(self):
        print(self.pay)

balck = Black_res('fdas','ysys','oqoq')
balck.prin_we_pay()
print(balck.year)

#we can reset the same name function in the son class
class City():
    """城市里面有好的饭店，也有坏的"""
    def __init__(self):
        self.b_rest = Black_res('uueee','china','tttt')

city = City()
print(city.b_rest.name)

#9-6冰淇淋小店
class IceCreamStand(Restaurant):
    """冰淇淋小店"""
    def __init__(self,name,type,*like):
        super(IceCreamStand, self).__init__(name,type)
        self.flavors = []
        for value in like:
            self.flavors.append(value)
    def display(self):
        for value in self.flavors:
            print(value)
ice = IceCreamStand('JJJ','TYTY','bing','binggun','xuebang')
ice.display()


#9-7
class Admin(User):
    """管理员"""
    def __init__(self,*str_list):
        super(Admin, self).__init__()
        self.privileges = []
        for value in str_list:
            self.privileges.append(value)

    def show_privileges(self):
        for value in self.privileges:
            print(value)

admin = Admin('can add post','can del post','an ban user')
admin.show_privileges()


from pizza import Car
car = Car('mode s')
car.display()

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    #del the line below

#file path
#pass

#read line by line
file_name = 'pi_digits.txt'
with open(file_name) as file_object2:
    for line in file_object2:
        print(line.rstrip())

with open(file_name) as file_object3:
    lines = file_object3.readlines()
for line in lines:
    print(line.rstrip())

with open(file_name) as file_object4:
    lines = file_object4.readlines()
pi_str = ''
for line in lines:
    pi_str += line.strip()
print(pi_str)
print(len(pi_str))

#replace
print(pi_str.replace('3.14','3.66'))
#temporary

#write txt
with open(file_name,'a') as file_object:
    for value in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
        file_object.write(str(value)+"\n")

# 10-3
# flag_quit = True
# while flag_quit:
#     ans = input("please enter your name \n if you want to quit enter 'quit' ")
#     if ans == 'quit':
#         break
#     elif ans == '':
#         print("please enter an non-empty ans")
#     else:
#         with open(file_name,'a') as file_object:
#             file_object.write(str(ans) + "\n")
# print("quited")
#

#10-4

try:
    print(5/1)
except ZeroDivisionError:
    print("you can't divide by zero!")
else:
    print("ans")


#File not found
#pass

#analyze txt
title = "Alice in Wonderland"
sp = title.split()
print(sp)

print(sp.count('in'))
#count

# import json
# num = [1,3,4,5,6,7]
# with open(file_name,'w') as file_object:
#     json.dump(num,file_object)
#
# with open(file_name,'r') as file_object:
#     u = json.load(file_object)
# print(u)
#
# username = input("please enter your name")
# with open(file_name,'w') as file_object:
#     json.dump(username,file_object)

#10-11
# def enter_num():
#     num = input("please enter a num")
#     with open(file_name,'w') as file_object:
#         json.dump(str(num),file_object)
#
# def get_num():
#     try:
#         with open(file_name) as file_object:
#              num = json.load(file_object)
#     except FileNotFoundError:
#         return input("please enter a num")
#     else:
#         return num
# enter_num()
# print(get_num())

#test code
def get_formatted_name(first,last):
    """生成整洁的名字"""
    full_name = first + " " + last
    return full_name.title()

print(get_formatted_name('j','jj'))

#data view
# import matplotlib.pyplot as plt
# squares = [1,4,9,16,25]
# plt.plot(squares)
# plt.show()

# #modify the line style
# import matplotlib.pyplot as plt
# #when we no set the pair of num
# squares = [1,4,9,16,25]
# input_num = [1,2,3,4,5]
# plt.plot(input_num,squares,linewidth = 5)
# plt.title("Hello",fontsize = 15)
# plt.xlabel("Value",fontsize = 14)
# plt.ylabel("Square of Value",fontsize = 14)
# plt.tick_params(axis='both',labelsize = 14)
# plt.show()
#

# import matplotlib.pyplot as plt
# input_num = list(range(1,1000))
# squares = [value **2 for value in input_num]
# # for value in input_num:
# #     squares.append(value**2)
# #删除数据点的轮廓
# plt.scatter(input_num,squares,s=1,edgecolors='none',c = squares,cmap = plt.cm.Blues)
# #设置图表标题并给坐标加上标签
# plt.title("Square Number",fontsize = 24)
# plt.xlabel("Value",fontsize = 14)
# plt.ylabel("Square of Value ",fontsize = 14)
# plt.axis([0,1100,0,1100000])
# #裁剪白色区域
# plt.savefig('svae.png')
#

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """一个生成随机漫步的属性"""
    def __init__(self,num_points = 5000):
        """初始化"""
        self.num_points = num_points

        #漫步始于（0,0）
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """计算所有的点"""
        while len(self.x) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的位置_使用上次最后一个数据进行新的计算
            next_x = self.x[-1]+x_step
            next_y = self.y[-1]+y_step

            self.x.append(next_x)
            self.y.append(next_y)

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x,rw.y,s=15,c = rw.x ,cmap=rw.cm.Blues)
plt.show()







