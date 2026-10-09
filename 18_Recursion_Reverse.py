# iterative approach
def reverse_string_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_from_end(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def reverse_string_using_list(s):
    return ''.join(reversed(s))

def reverse_string_using_slice(s):
    return s[::-1]

# recursive approach
def reverse_string_recursive(s):
    if not s:
        return ""
    else:
        return reverse_string_recursive(s[1:]) + s[0]


myString = "Hello, World!"

result_iterative = reverse_string_iterative(myString)
print("Reversed string (iterative):", result_iterative)

result_from_end = reverse_string_from_end(myString)
print("Reversed string (from end):", result_from_end)

result_recursive = reverse_string_recursive(myString)
print("Reversed string (recursive):", result_recursive)

result_using_list = reverse_string_using_list(myString)
print("Reversed string (using list):", result_using_list)

result_using_slice = reverse_string_using_slice(myString)
print("Reversed string (using slice):", result_using_slice)
