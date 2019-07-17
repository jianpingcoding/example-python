# -*- coding: utf-8 -*-

import os

pid = os.fork()
if pid == 0:
    print("this is the child")
elif pid > 0:
    print("the child is pid %d" % pid)
else:
    print("An error occured")
