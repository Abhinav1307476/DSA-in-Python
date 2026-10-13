def BubbleSort_decreasing(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is less than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = BubbleSort_decreasing(arr)
print("Sorted array:", sorted_arr)