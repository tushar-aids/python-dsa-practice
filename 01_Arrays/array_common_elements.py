# Find common elements between two arrays

arr1 = [10, 20, 30, 40, 50]
arr2 = [30, 50, 70, 90]

# Using set intersection
common = list(set(arr1) & set(arr2))

print("Common elements:", common)



# output:
# Common elements: [50, 30]
