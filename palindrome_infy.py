initial_num = eval(input())
while True:
    print(initial_num)
    if str(initial_num)[::-1] == str(initial_num):
        print(initial_num)
        break
    else:
        initial_num += int(str(initial_num)[::-1])

    