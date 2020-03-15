def getTotalX(a, b):
    result = []
    for i in range(1,min(b)+1):
        for j in a:
            if i%j != 0:break
        else:
            for j in b:
                 if j%i != 0:break
            else:result.append(i)       
    return len(result)

print(getTotalX([2, 4],[16, 32, 96]))