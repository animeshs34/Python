import math
def pageCount(n, p):
    pages_count_pos = 0
    pages_count_neg = 0
    for i in range(1,n+1,2):
        if p in [i,i-1]:
            break
        else:
            pages_count_pos += 1
    for i in range(n,0,-1):
        if p in [i]:
            break
        elif i%2 == 0:
            pages_count_neg += 1
    
    return min(pages_count_pos,pages_count_neg)
    
print(pageCount(6,5))