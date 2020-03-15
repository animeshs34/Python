fibbonaci = lambda n: n if n in (0,1) else fibbonaci(n-1) + fibbonaci(n-2)
print(fibbonaci(11))