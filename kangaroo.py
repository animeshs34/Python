def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

print(kangaroo(1571, 4240 ,9023 ,4234))
print(kangaroo(7271 ,2211 ,7915 ,2051))
print(kangaroo(1928, 4306, 5763, 4301))
