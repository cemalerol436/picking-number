
def pickingNumbers(arr):

    arr.sort()
    array_sorted = list(set(arr))

    final_result = 0

    for index in arr:
        rst = arr.count(index)
        if rst >final_result:
            final_result = rst

    i = 0

    while i<len(array_sorted):

        if i!=0 and -1 <= array_sorted[i-1]-array_sorted[i] <= 1 :
            res = (arr.count(array_sorted[i])) + (arr.count(array_sorted[i - 1]))
            if res>final_result:
                final_result = res
        i += 1
    return final_result

arr = list(map(int, input("Type an array:").rstrip().split()))

result = print(pickingNumbers(arr))
