def staircase(n):

    print("\n".join([" "*(n-i)+"#"*i for i in range(1,n+1)]))

staircase(6)