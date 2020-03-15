def TowerOfHanoi(n, frompeg, topeg, aux):

    if n == 1:
        print("Move disk 1 from {} to {}".format(frompeg, topeg))
        return
    else:
        TowerOfHanoi(n-1, frompeg, aux, topeg)
        print("Move {} disk from {} to {}".format(n, frompeg, topeg))
        TowerOfHanoi(n-1, aux, topeg, frompeg)


TowerOfHanoi(5, "A", "B", "C")