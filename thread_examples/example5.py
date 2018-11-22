#!/usr/bin/env python3

import threading
import time
list1 = []

def fun1(a):
    print(".")
    time.sleep(1) # complex calculation takes 1 seconds
    list1.append(a)

thread1 = threading.Thread(target = fun1, args = (1, ))
thread1.start()
thread2 = threading.Thread(target = fun1, args = (6, ))
thread2.start()
thread1.join()
thread2.join()

print("List1 is: ", list1)
