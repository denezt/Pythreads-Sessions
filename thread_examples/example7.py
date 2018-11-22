#!/usr/bin/env python3
# join() Method With Time
#

import threading
import time

def fun1(a):
    time.sleep(3) # complex calculation takes 3 seconds

thread1 = threading.Thread(target = fun1, args = (1, ))
thread1.start()
thread1.join()

print(thread1.isAlive())
