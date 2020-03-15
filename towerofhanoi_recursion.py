def TowerOfHanoi(n,source,aux,target):
    if n == 1 :
        print("Move disk 1 from {} to {}".format(source,target))
        return " "

    TowerOfHanoi(n-1,source,target,aux)
    print("Move disk {} from {} to {}".format(n,source,target))
    TowerOfHanoi(n-1,aux,source,target)

#TowerOfHanoi(5,"A","B","C")

TOH = lambda n,a,b,c : "Move disk 1 from {} to {}".format(a,c) if n == 1 else print(TOH(n-1,a,c,b),"Move disk {} from {} to {}".format(n,a,c),TOH(n-1,b,a,c),sep = "\n")
TOH(5,"A","B","C")