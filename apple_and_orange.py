def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([i for i in apples if s<=i+a<=t]),len([i for i in oranges if s<=i+b<=t]),sep='\n')
    
countApplesAndOranges(s = 2, t = 3, a = 1 ,b = 5, apples=[2],oranges=[-2])