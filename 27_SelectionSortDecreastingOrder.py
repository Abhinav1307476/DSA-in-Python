def SelectionSort_decreasing(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


arr = [64, 35, 2, 26, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = SelectionSort_decreasing(arr)
print("Sorted array:", sorted_arr)