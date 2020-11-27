"""""
#tuples are immutable

a = 10,20,30
print(a)


b = 1,2,3,4,5,6,7,8,9
print(b)

print(b[:8])

c = (10,10,20,30,[23,45,56])

print(c)
c[1] = 34
print(c[-1][1])

d = c+b
print(d)

print(d.count(10))

print(d.index(10))

#tuple constructor

a = [1,2,3]

print(a)

print(tuple(a))

## Iterating through a tuple

a = (1,2,3,4,5,6,7,8,9)

for i in a:
    print(i)

# membership test

print(a)

print(9 in a)

for i in a:
    j=i
    if j in a:
        print(j)


import random

n = 1000
guess_it = int(n*random.random() +1)
guess = 0

while guess != guess_it:
    guess = int(input("New Number : "))
    if guess >0:
        if guess > guess_it:
            print("Number too large")
        elif guess < guess_it:
            print("Number too small")
    else:
        print("Sorry that you're giving up")
        break
else:
    print("Congratulation  , You made it")


fruits = ['mango','grape','apple']

for fruit in fruits:
    print(fruit)
print(fruit)


num = int(input("Number : "))
factorial = 1

for i in range(1,num+1):
    factorial = factorial*i
print(factorial)

"""""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 5)
print(t)
y = np.array([1, 2, 3.5, 10, 20])
print(y)
#plt.plot(t,y,"ro")
# plt.show()
