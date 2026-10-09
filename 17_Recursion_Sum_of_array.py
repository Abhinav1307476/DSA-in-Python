def sum_of_array(arr):
    total = 0
    for item in arr:
        total += item
    return total

# python stuff
def sum_of_array_in_python(arr):
    return sum(arr)

# more python stuff
def sum_of_array_in_python_list_comprehension(arr):
    total = 0
    [total := total + x for x in arr]
    return total

def recursive_sum_of_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum_of_array(arr[1:])
    
x = [1, 2, 3, 4, 5]
result = sum_of_array(x)
print("The sum of the array is:", result)
python_result = sum_of_array_in_python(x)
print("The sum of the array (in Python) is:", python_result)

recursive_result = recursive_sum_of_array(x)
print("The sum of the array (recursive) is:", recursive_result)

list_comprehension_result = sum_of_array_in_python_list_comprehension(x)
print("The sum of the array (list comprehension) is:", list_comprehension_result)



