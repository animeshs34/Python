def countingValleys(s):
    position = 0
    valley = -1
    for i in s:
        print(valley,i)
        if position == 0:
            valley += 1
        if i == "U":
            position = position + 1
        elif i == "D":
            position = position - 1
        print(valley)
    return valley

#print(countingValleys("UDDDUDUU"))
print(countingValleys("UDUUUDUDDD"))
