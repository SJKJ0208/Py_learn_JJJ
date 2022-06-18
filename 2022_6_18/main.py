# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#learn impact new mode
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












