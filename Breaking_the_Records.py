def breakingRecords(scores):
    rec_breaked_up = 0
    rec_breaked_down = 0
    min = max = scores[0]
    for i in scores[1:]:
        if i > max:
            max = i
            rec_breaked_up += 1
        elif i < min:
            min = i
            rec_breaked_down += 1
        else:
            pass
    return [rec_breaked_up,rec_breaked_down]

print(breakingRecords([10,5,20,20,4,5,2,25,1]))
