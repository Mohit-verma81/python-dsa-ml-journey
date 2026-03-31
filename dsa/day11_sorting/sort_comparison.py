import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = list(range(1000, 0, -1))

start = time.time()
bubble_sort(arr.copy())
print("Bubble Sort Time:", time.time() - start)

start = time.time()
sorted(arr)
print("Built-in Sort Time:", time.time() - start)