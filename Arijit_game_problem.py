import re
T = eval(input())
TC = []
for i in range(T):
    TC.append(input())
for i in TC:
    print(list(re.sub("OX|XO","X",i)).count("O"))