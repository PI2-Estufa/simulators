import time 
import random

temperature = 20

while True:
    time.sleep(1)
    temperature = random.randint(20, 30) + random.random()
    print("%.2f" % temperature)
