'''
Created on Feb 4, 2017
@author: loanvo

Description:
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import string

alist = list(range(1, 5))
print('alist:', alist)
asquaredlist = [i * i for i in alist]
print('asquaredlist:', asquaredlist)
print('enumerate(asquaredlist):', *enumerate(asquaredlist))
print('zip(alist,asquaredlist):', *zip(alist, asquaredlist))

with open('hamlet.txt', 'rt', encoding='UTF-8') as hamletfile:
    hamlettext = hamletfile.read()
    hamlettokens = hamlettext.split()
# print(hamlettext)
# print(type(hamlettext))
print(len(hamlettokens))

# The indexing of lists
print(hamlettext[:100])  # first 100 characters from Hamlet
print(hamlettext[-100:])  # last 100 characters from Hamlet
print(hamlettokens[1:8:2])  # get every 2nd world between the 2nd and the 9th: ie 2nd, 4th, 6th, and 8th

# Dictionary
adict = {'one':1, 'two':2, 'three':3}
print('dict: key of each and every item in dict:', [i for i in adict])
print('dict.items(): key and value pair of each and item in dict:', [(k, v) for k, v in adict.items()])
print('dict.values(): Values in dict:', [v for v in adict.values()])
# construct dict 
mydict = {k:v for k, v in zip(range(5), string.ascii_lowercase[:5])}
print(*mydict.items())
# construct dict
mydict2 = dict(a=1, b=2)
print(*mydict2.items())


# String
lastword = hamlettokens[-1]
print('Last word:', lastword)
print(lastword[-2])
try:
    lastword[-2] = 'k'
except:
    import sys
    print('Cannot change a part of a string. The following gives error: lastword[-2] = "k"')
    print(sys.exc_info())
wierdstring = ','.join(hamlettokens[:200])
print(wierdstring)



# Functions
def square(x):
    return x * x
import math
def cube(x):
    return math.pow(x, 3)
print(square(3))
print(cube(2))
# In Python, you can pass functions to other functions
def sumOfAnything(x, y, f):
    return f(x) + f(y)

# Python functions can have positional arguments and keyword arguments. Positional arguments are stored in a tuple, and keyword arguments in a dictionary. Note the "starred" syntax
def funcWithPositionalAndKeywordArgurments(x, y, *posArg, **keyArg):
    print('Input argurments:', x, y, posArg, keyArg)
    return None
funcWithPositionalAndKeywordArgurments(5, 7)  # this function requires at least two input arguments x and y
funcWithPositionalAndKeywordArgurments(5, 7, 4, 8, 3, one=1, two=2)
