#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    # Write your code here
    contador,negacontador,cerocontador = 0,0,0
    for i in arr:
        if i > 0:
            contador = contador + 1
        elif i < 0:
            negacontador = negacontador + 1
        else:
            cerocontador = cerocontador + 1

    contador = contador / len(arr)
    negacontador = negacontador / len(arr)
    cerocontador = cerocontador / len(arr)

    print("{:.6f}\n{:.6f}\n{:.6f}".format(contador,negacontador,cerocontador))


plusMinus(arr)
