import random

# 6 kapı
def selectDoor():
    number = random.randint(0,5)
    return number

def carDoor():
    return selectDoor()


def compare():
    usersDoor = selectDoor()
    carDoor = selectDoor()
    return (usersDoor == carDoor)

def calc(n):
    equal = 0
    notEqual = 0
    count = 1
    div = n
    while(n > 0):
        n -= 1
        if(compare()):
            equal += 1
        else:
            notEqual += 1

    return(notEqual / div, equal / div)

notEqual, equal = calc(100000)
print("Değiştirirse: " + str(notEqual))
print("Değiştirmezse: " + str(equal))