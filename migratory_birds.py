def migratoryBirds(arr):
    frequency_count = {i:arr.count(i) for i in arr}
    return max(frequency_count, key=frequency_count.get)