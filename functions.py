import random as r

def sumlist(list):
    sum = 0
    for i in list:
        if type(i) == float or type(i) == int:
            sum += i
    return sum

def randatt(min=20,max=99):
    return r.randint(min,max)
