# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

message = "JJJ is man"
print(message)

message = "Hwm is girl"
print(message)

message =  "'lie' is not allowed "
print(message)

message = "lie"
print(message)

print(message.upper())
print(message.lower())

first_name = "J"
last_name = "JJ"
full_name  = first_name + " " +last_name
print(full_name.title())#title will set the first lettle upper

print("Python")
print("\tPython")
print("Py\nthon")

message = "python  "
print(message)

print(message.rstrip())

message = message.rstrip()
print(message)

name = "Eric"
print("Hello " + name +",would you like to learn some Python today?")

print(name.upper())
print(name.lower())
print(name.title())

motto = 'Albert Einstein once said "Everyone is a fool"'
print(motto)

age = 20
name = "JJJ "
say = " Happy Birthday!"
#print(name + age + say)
print(name + str(age) + say)

#import this

#List
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
#how to find the ele

print(bicycles[0])

print(bicycles[0].title())

#how to learn the '-1'—— -1 is the index of the last one
#-2 is the index of 倒数第二个
print(bicycles[-1])

#3-1
names = ['Hwm','Hwf','Hyh']
print(names[0]+"\n"+names[1]+"\n"+names[2])

#3-2
say_hi = "hi "
print(say_hi+names[0])
print(say_hi+names[1])
print(say_hi+names[2])

#change the ele of list
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

motocycles[0] = "+0崽"
print(motocycles)

motocycles.append('+0崽2')
print(motocycles)

#the int will be the index of new str
motocycles.insert(0,' insert')
print(motocycles)

#del
del motocycles[3]
print(motocycles)

#pop
ele_poped = motocycles.pop()
print(ele_poped)
print(motocycles)


#pop the ele which we selected
ele_poped = motocycles.pop(0)
print(ele_poped)
print(motocycles)

#del will not get the ele which you del
#you will get the ele which you pop out

motocycles.remove('yamaha')
print(motocycles)
#it just remove the first ele which program met

#3-4
guest = ['Hwm','Hyh','Hrc','Hwf']
print('i will invite '+guest[0])
print('i will invite '+guest[1])
print('i will invite '+guest[2])
print('i will invite '+guest[3])

#3-5
print(guest[2]+" is unavailable")
n = 2
guest.insert(2,'HHH')
guest.pop(n+1)
print(guest)

#3-6
print("we find more biger than before , we can invite more people than before")
guest.insert(0,'HYY')
print(guest)
guest.insert(2,'YYY')
print(guest)
guest.append('PPP')
print(guest)
print('i will invite '+guest[0])
print('i will invite '+guest[1])
print('i will invite '+guest[2])
print('i will invite '+guest[3])
print('i will invite '+guest[4])
print('i will invite '+guest[5])
print('i will invite '+guest[6])


#3-7
print("since we can't get so much tableware,we can only invite two people")
pop_guest = guest.pop()
print("sorry "+pop_guest + " we can't invite you ")
pop_guest = guest.pop()
print("sorry "+pop_guest + " we can't invite you ")
pop_guest = guest.pop()
print("sorry "+pop_guest + " we can't invite you ")
pop_guest = guest.pop()
print("sorry "+pop_guest + " we can't invite you ")
pop_guest = guest.pop()
print("sorry "+pop_guest + " we can't invite you ")
print(guest)

print(guest[0] + " welcome")
print(guest[1] + " welcome")

del guest[0]
del guest[0]

print("the guest : " + str(guest))


#Group List

#sort by the first ele
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#reverse the sort rules
cars.sort(reverse=True)
print(cars)

#use the sorted to sort the list temporary
print(cars)
print("sort of temporary " + str(sorted(cars)))
print("after " + str(cars))
print("sort of temporary and reserve " + str(sorted(cars,reverse=True)))
print("after " + str(cars))

#print the list by reversed
print(cars)
cars.reverse()
print(cars)
#we can recover by set reverse again
cars.reverse()
print("recover ：" +str(cars))

#we find the len of list
n = (len(cars) + 1)/2
print(n)
print(len(cars))

#3-8
scene = ['BeiJing','ShangHai','HongKong']
print(scene)
print(sorted(scene))
print(scene)
print(sorted(scene,reverse=True))
print(scene)
scene.reverse()
print(scene)
scene.reverse()
print(scene)
scene.sort()
print(scene)
scene.sort(reverse=True)
print(scene)

#3-9
print(len(scene))

#3-10
#we get it

magicians = ['alice','david','carolina']
for magician in  magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + " ,that was a great trick!")
    print("i can't not to wait to see " + magician.title() +" next trick")
print("thank you")

pizzas = ['pz1','pz2','pz3','pz4']
for pizza in pizzas:
    print("i like "+ pizza)
print("i really like pizza")

#4-2
cats = ['lions','cat','leopard']
for cat in cats:
    print(cat)

#creat a num list
for value in range(1,5):
    print(value)
#if you want to print the num from one to five
for value in range(1,6):
    print(value)

#use the command of range to create the num list
numbers = list(range(1,6))
print(numbers)

#we can set the step of the range
numbers = list(range(1,10,2))
print(numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#we can find the max and min num in the list easily
digits = []
for value in range(1,11):
    digits.append(value)
print(min(digits))
print(max(digits))
print(sum(digits))

#List of analytical
squares = [value**2 for value in range(1,11)]
print(squares)

#4-3
for value in range(1,21):
    print(value)

#4-4
num_list = [value for value in range(1,1000001)]
# for value in num_list:
#     print(value)

#4-5
print(min(num_list))
print(max(num_list))
print(sum(num_list))

#4-6
odd_num = [value for value in range(1,21,2)]
for value in odd_num:
    print(value)

#4-7
division_3 = []
for value in range(3,31):
    if value % 3 == 0:
        division_3.append(value)
print(division_3)

#4-8
cube = [value**3 for value in range(1,11)]
print(cube)

#4-9
#as described above

#we will control the section of list
players = ['charles','martina','michael','florence','eli']
print(players)
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[:])
print(players[-3:])

#we use for to traverse the section of list
for player in players[:]:
    print(player)

#we copy the list
#ues the section of list to copy list as copy the double of place
#Just to use the equal to copy as send the same place to a new pointer
like_players = players[:]
print(like_players)

#4-10
message = "items in the list are:"
print("full" + str(players))
print("the first three " + message + str(players[0:3]))
print("Three items from the middle of the list art :" + str(players[2:]))
print("The last three items in the list are:"+ str(players[-3:]))

#4-11
friend_pizzas = pizzas[:]
pizzas.append('new_pizza')
friend_pizzas.append('another_pizza')
print("my - pizza"+str(pizzas))
print("friends - pizza" + str(friend_pizzas))

#4-12
for value in pizzas:
    print(value)

#tuple
#tuple can't not change by the user but list can
#tuple look like list

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 1
# print(dimensions)
#tuple can't change

for dimension in dimensions:
    print(dimension)

#we can't change the contain of tuple,but we can reset the tuple by ourselves

print(dimensions)
dimensions = (300,20)
print(dimensions)

#4-13
tuple_buffer = (1,2,3,4,5)
for value in tuple_buffer:
    print(value)
tuple_buffer = (1,2,3,6,7)
for value in tuple_buffer:
    print(value)

#we learn the if sentence
#we just test the and or
if (1>=1 and 2>1) or 0 > 1:
    print("succeed")

#we just test the code 'in'
if 1 in tuple_buffer:
    print("we can eat this 1")

#we test the code 'not in'
if 8 not in tuple_buffer:
    print("we can't eat the 8")

#5-1
#pass

age = 99
if age > 18:
    print("adult")
else:
    print("not adult")

if age > 5 and age < 18:
    print("you are teenage")
elif age >18:
    print("you are adult")
else:
    print("you just a baby")

#we should use elif to instant the else

#5-3
alien_color = 'green'
if alien_color == 'green':
    print("you get 5 starts")

if alien_color != 'green':
    print()

#5-4
alien_color = 'red'
if alien_color == 'green':
    print("you get 5 starts")
else:
    print("you get 10 starts")

#5-5
if alien_color == 'green':
    print("5 starts")
elif alien_color == 'red':
    print("10 starts")
elif alien_color == 'red':
    print("15 starts")

#5-6
#pass

#we can use if to analyze if the list is empty
empty_list = []
if empty_list:
    print("the list is full")
else:
    print("the list is empty")

#5-8
#5-9
acount = ['admin','jjj','hwm','hrc','hyh']
log = 'sss'
if acount:
    if log in acount:
        if log == 'admin':
            print("hello admin")
        elif log != 'admin':
            print("hello "+log)
    elif log not in acount:
        print("sorry enter error")
else:
    print("acount is empty")

#5-10
current_users = acount[:]
new_users = acount[:]
del new_users[3]
del new_users[1]
del new_users[2]
new_users.append('HWM')
new_users.append('hhh')
for value in new_users:
    if value.title() in current_users or value.lower() in current_users or value.upper() in current_users:
        print("can not use this name " + value)
    else:
        print("yes ok")

#5-11
numbers = list(range(1,10))
for value in numbers:
    #print(value)
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(str(value) + "th")

#Dictionary
alien_0 = {'color' : 'green','points' : 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 255
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

alien_0['speed'] = 'medium'
print("origin x = " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

print("now x = "+str(alien_0['x_position']+x_increment))

#dictionary del
print(alien_0)
del alien_0['speed']
print(alien_0)

#format
languages = {
    'jjj' : 'hwm'
}
print(languages)
#6-1
din = {
    'first_name' : 'J',
    'last_name' : 'JJ',
    'age' : 20,
    'city' : 'ZC'
}
print(din)
#6-2
#tranverse the dinctionary
#tranverse the key-value
for key,value in din.items():
    print("\n key :" + key)
    print("value : " + str(value))

#just tranverse the keys in dictionary
for key in din.keys():
    print("all keys : " + str(key))

#so as
for value in din.values():
    print("all value : " + str (value))

#get the list of keys
keys = din.keys()
print(keys)

print(sorted(din))

#we can set the list to set
#because set just can save the ele once in the same set
same_list = [1,2,3,4,4,4,4,4]
once_set = set(same_list)
print(once_set)


#6-4
name_py = {
    'set':'集合',
    'list':'列表',
    'dictionary':'字典',
}
for name,explain in name_py.items():
    print(str(name) + " is mean : " + str(explain))

#nest
#save the dictionary in list or save the list in dictionary
print(alien_0)
alien_1 = alien_0.copy()
alien_2 = alien_0.copy()
aliens = [alien_0,alien_1,alien_2]
print(aliens)

boy = {
    'cars':['moto','+0崽'],
    'wife':'hwm',
    'us':'gdut'
}

print("\nhe boy's wife named: "+
      str(boy['wife'])+
      "his us is : "+
      str(boy['us'])+
      "and he have cars :"
      )

for car in boy['cars']:
    print("\t"+ car)

#6-7
din = {
    'first_name' : 'J',
    'last_name' : 'JJ',
    'age' : 20,
    'city' : 'ZC'
}
print(din)
din_peo1 = {
    'first_name': 'J',
    'last_name': 'JJ',
    'age': 20,
    'city': 'ZC'
}
din_peo2 = {
    'first_name': 'H',
    'last_name': 'WM',
    'age': 21,
    'city': 'ZC'
}
din_peo3 = {
    'first_name': 'H',
    'last_name': 'JH',
    'age': 23,
    'city': 'ZC'
}
people = [din_peo1,din_peo2,din_peo3]
print(people)
for peo in people:
    print("\n")
    for key,value in peo.items():
        print(str(key)+"   "+str(value))

#learn input and while
# message = "Tell me something , i will back you"
# message += "please give me your name "
# name = input(message)
# print("your name is :" + name)

#if we want to get a num ,we should transform it
# message = "please tell me your name"
# age  = input(message)
# age = int(age)
# if age > 18:
#     print("you are an adult")

# counter = 1
# while counter < 10000:
#     counter += 1
#     print(counter)
#

# unconfig = ['sss','ffff','aaaa','tttt']
# config = []
# while unconfig:
#     tmp = unconfig.pop()
#     print(tmp)
#     config.append(tmp)
# print(unconfig)
# print(config)
#
# responses = {}
# flag_active = True
# while flag_active:
#     name = input("name")
#     ans = input("ans")
#     responses[name] = ans
#     if input("quit ? ") == 'quit':
#         flag_active = False
# print(responses)

#7-8
sandwich_orders = ['j1','j2','j3']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("i made " + sandwich)
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)


def greet_user():
    """现实简单的问候语"""
    print("Hello")
greet_user()

def greet_user(username):
    """def"""
    print("name is :" + username.title())
greet_user("jjj")

#position pass key-we try
def describe_pet(animal_type,pet_name):
    """display_animal"""
    print(animal_type)
    print(pet_name)
describe_pet(animal_type='pppp',pet_name='kkk')

#we set the variable in def and we can reset it when we call it up
#we must declare have not set variable at front
def describe_pet(animal = 'kkk',name = 'hhh'):
    print(animal)
    print(name)
describe_pet(animal='yyy',name='ttt')

#8-3
def make_shirt(size,font):
    print(size)
    print(font)
make_shirt(12,36)

#back_call variable
def get_formatted_name(first_name,last_name):
    """返回整洁的名字"""
    full_name = first_name + ' '+last_name
    return full_name.title()
full_name = get_formatted_name('J','JJ')
print(full_name)

#we can set a not necessary
def get_formatted_name(first_name,last_name,mid_name = ''):
    """返回整洁的名字"""
    if mid_name:
        full_name = first_name + ' ' + mid_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
full_name = get_formatted_name('J','JJ','焯')
print(full_name)

def build_person(first_name,last_name):
    """测试返回字典"""
    person = {'first_name':first_name,'last_name':last_name}
    return person
musician = build_person('J','jj')
print(musician)

def build_person(first_name,last_name,age = ''):
    person = {'first_name' : first_name,'last_name':last_name}
    if age:
        person['age'] = age
    return person
print(build_person('sss','ddd',32))

#send a list to function
def greet_users(names):
    """尝试向函数中传入列表"""
    for name in names:
        message = name + " Hello"
        print(message)
greet_users(['jjj','hwm','kkk'])


#modify the list we sent into the function
before_list = ['lll','jjj','hhh']
modify_list = []
def prin_list(send_list):
    for ele in send_list:
        print(str(ele))
def prin_models(before_list,modeify_list):
    """在函数中修改列表"""
    while before_list:
        ele = before_list.pop()
        print("we finish" + str(ele))
        modeify_list.append(ele)
    prin_list(before_list)
    prin_list(modeify_list)
prin_models(before_list,modify_list)

#we can send a can't modify list in the function
#so we should copy the list into the function
prin_models(before_list[:],modify_list[:])
#as above we send the copy into the function

#send Transmit variable length parameters
def known_no_variables(*variables):
    for variable in variables:
        print(variable)
known_no_variables('jjjjjj','pppppp')

def known_no_variables(name,age,*variables):
    print(name)
    print(age)
    for variable in variables:
        print(variable)
known_no_variables('jjj',12,'fdas','fdfd')

#send in a pair of key-value
def build_profile(first,last,**user_info):
    """创建一个字典，包含我了结的所有事情"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
new_users = build_profile('J','JJ',cars = ['car1','car2'],key = 'value')
print(new_users)

#8-12
def build_sandwich(*compont):
    for value in compont:
        print(value)
build_sandwich('fdsaf','fdsafegggg','eeee')

#8-13
#pass

#inpact mode



