N = eval(input())
A = [int(i) for i in input().split(" ")]
Q = eval(input())
q = [tuple(map(int, input().split(" "))) for i in range(Q)]

for i in q:
    temp = []
    if i[0] == 0:
        for j in A:
            if not j < i[1]:
                temp.append(j)
        print(len(temp))
    elif i[0] == 1:
        for j in A:
            if j > i[1]:
                temp.append(j)
        print(len(temp))
