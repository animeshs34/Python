T = eval(input())
test_cases = []
for i in range(T):
    X, Y, Z = input().split(' ')
    test_cases.append([int(X), int(Y), int(Z)])

for i in test_cases:
    result = i[0]*i[1] + i[1]*i[2] + i[0]*i[2] + i[0]*i[1] + i[1]*i[2] + i[0]*i[2]
    print(result)
