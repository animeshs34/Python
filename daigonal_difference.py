import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    ld = rd = 0
    for i in range(n):
        for j in range(n):
            if j == i: 
                ld += arr[i][j]
                print(ld,i,j,"ld")                
            if j == ((n-1) - i):
                rd += arr[i][j]
                print(rd,i,j,"rd")
                
    return abs(ld-rd)


arr = [[11,2,4],[4,5,6],[10, 8 ,-12]]

print(diagonalDifference(arr))