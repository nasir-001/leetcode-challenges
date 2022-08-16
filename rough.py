import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    for i in range(n):
        steps = steps * math.ceil(n/5.0)
        if steps == 0:
            steps += 1
    print(steps)
print(time(6))

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print(y)

print(countdown(50))