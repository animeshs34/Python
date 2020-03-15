from itertools import permutations
from functools import reduce

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if reduce(lambda x,y : x+y,s[i:i+m]) == d:
            count += 1
    return count
