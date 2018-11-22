#!/usr/bin/env python3
# Python Thread Creation Using a Function
#

import threading

def fun1(a, b):
    c = a + b
    print(c)

thread1 = threading.Thread(target = fun1, args = (12, 10))
thread1.start()
