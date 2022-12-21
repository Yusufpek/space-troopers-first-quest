import random
lamps = [False] * 6

def r():
    return random.randint(0,5)

def check():
    for l in lamps:
        if(not l):
            return False
    return True

def calc():
    count = 0
    while(not check()):
        count += 1
        i = r()
        lamps[i] = not lamps[i]
    return count

def clear():
    global lamps
    lamps = [False] * 6

def average(n):
    div = n
    result = 0
    while(0 < n):
        result += calc()
        clear()
        n -= 1
    return result / div

print(average(1000000))