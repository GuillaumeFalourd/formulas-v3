#!/usr/bin/python3
import os
import random

def run():
    n = str(random.random())
    cmd = "mkdir test" + n
    os.system(cmd)
    print("Template created!")
