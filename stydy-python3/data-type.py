num = 123
# type() 是py内置的函数，用于检测数据是哪种类型
print(type(num)) # <class 'int'>
print(isinstance(num, int)) # True

boolNum = True
print(type(boolNum)) # <class 'bool'>
print(isinstance(boolNum, bool)) # True

complexData = 1+2j
print(type(complexData))
print(int(10.11))

# 数学常量
from math import pi, e, log
print(e)
print(pi)

# 数学函数
print(abs(-1000)) # 数学函数，直接使用即可
print(log(10))

# 数字的运算
print(10/5) # 2.0
print(10//5) # 2
print(10//3) # 3
print(11//3) # 2

# py下常用的生成随机数的函数
from random import random, choice
print('随机数 ===>>>');
print(random()) # 	随机生成下一个实数，它在[0,1)范围内。
print(choice(range(10))) # 随机从0-9中返回一个数据
