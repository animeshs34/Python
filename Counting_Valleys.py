def countingValleys(s):
    position = 0
    valley = 0
    for i in s:
        if i == "U":
            position += 1
            if position == 0:
                valley += 1
        else:
            position -= 1
    return valley

