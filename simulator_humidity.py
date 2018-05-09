import time 
import random

humidity = 50

while True:
    time.sleep(1)
    humidity = random.randint(20, 95)
    print("%d%%"  %humidity)
