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
make_pizza()
#we should not use it


#
