from time import sleep
from emoji import emojize
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print("\033[1;31mPOW POW POW POW")
print(emojize(":fire::fireworks::fire:"))
