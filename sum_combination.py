import itertools,functools
max = l = 0
for i in list(itertools.permutations([int(i) for i in input().split(",")],3)):
    l += 1
    num = int(functools.reduce(lambda sum,ele: sum * 10 + ele, i))
    max = num if num > max else max

print(max,l,sep=",")

