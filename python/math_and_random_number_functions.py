#!/usr/bin/python

import math
import random

x=13.65
y=-11
z=10

print('abs(-11): ', abs(y))
print('ceil(13.65): ', math.ceil(x))
print('floor(13.65): ', math.floor(x))
print('max(13.65,-11,10): ', max(x,y,z))
print('min(13.65,-11,10): ', min(x,y,z))
print('round(13.65): ', round(x))
print('modf(13.65): ', math.modf(x))
print('sqrt(10): ', math.sqrt(z))
# print('cmp(10,13.65): ', cmp(z,x)) The cmp() method has been deprecated in Python 3.x. The workaround is ((a>b)-(a<b))
print((10>13.65)-(10<13.65))  
print('log10(10): ', math.log10(z))
print('log(10): ', math.log(z))
print('exp(10): ', math.exp(z))

print('----random number functions----')
print('choice(13.65,-11,10): ', random.choice((x,y,z)))     # We used a tuple (x,y,z)
print('random choice in a string \"Hello World\": ', random.choice('Hello World'))
print('randrange(100,1000,3): ', random.randrange(100,1000,3))
print('generating a random float r such that 0<=r<1: ', random.random())
print('generating another random float: ', random.random())

print('---now we will generate random floats with seed 10---')
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
random.seed(10)         # notice that we repeated seed().We will get same random float as output in all 3 cases
print(random.random()) 

list = [1,21,6,654]
random.shuffle(list)
print('randomly shuffled list [1,21,6,654]: ', list)

print('random float between 5 and 10: ', random.uniform(5,10))
print('-----now experimenting with seed-----')
random.seed(10)
print(random.uniform(5,10))
random.seed(20)
print(random.uniform(5,10))
