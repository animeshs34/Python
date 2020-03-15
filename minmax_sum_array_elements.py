import functools
def miniMaxSum(arr):
    arr = sorted(arr)
    max = functools.reduce(lambda a,b: a + b,arr[1:])
    min = functools.reduce(lambda a,b: a +b,arr[0:(len(arr)-1)])
    print(min,max)

miniMaxSum([1,2,3,4,5])
    