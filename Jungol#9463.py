def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if i != n - 1:
            for k in arr:
                print(k, end = " ")
        print("")
I = list(map(int, input().split()))
bubbleSort(I)
