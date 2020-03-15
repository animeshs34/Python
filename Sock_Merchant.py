def sockMerchant(ar):
    pairs = 0
    for i in list({i:ar.count(i) for i in ar}.values()):
        pairs += i//2
    return pairs

print(sockMerchant([10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20]))