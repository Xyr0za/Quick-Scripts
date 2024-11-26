import random
from datetime import datetime

def roll():
    return random.randint(1,6), random.randint(1,6)

p1 = 0
p2 = 0
p3 = 0

mir = 10_000_000

beg = datetime.now()

for i in range(0,mir):
    i = 0
    while True:
        a,b = roll()
        if a + b == 7:
            if i%3 == 0:
                p1 += 1
            elif i%3 == 1:
                p2 += 1
            else:
                p3 += 1
            break
        i += 1

end = datetime.now()

print(end - beg)

print(f"{p1=} {p2=} {p3=}")
print(p2 / mir)
