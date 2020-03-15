def fibonacci(n):
    series = []
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        series.append(a)
        series.append(b)
        for i in range(2,n):
            series.append(series[i-1] + series[i-2])
    return series

print(fibonacci(10))