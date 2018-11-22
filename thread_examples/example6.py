#!/usr/bin/env python3

import threading
import time
import datetime

t1 = datetime.datetime.now()
list1 = []

def fun1(a):
    time.sleep(1) # complex calculation takes 1 seconds
    list1.append(a)

list_thread = []

for each in range(10):
    thread1 = threading.Thread(target = fun1, args = (each, ))
    list_thread.append(thread1)
    thread1.start()

for th in list_thread:
    th.join()

print("List1 is: ", list1)
t2 = datetime.datetime.now()
print("Time taken", t2 - t1)

