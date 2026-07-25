#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input(""))
num = n%2

if num !=0:
    print("Weird")
elif num==0 and n>=2 and n<=5:
    print("Not Weird")
elif num==0 and n>=6 and n<=20:
    print("Weird")
elif num==0 and n>20:
    print("Not Weird")
elif n<1 or n>100:
    print("Please enter a positive integer in the inclusive range [1,100]")
