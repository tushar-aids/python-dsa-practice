# Merge two arrays into one

arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

# Method 1: Using + operator
merged1 = arr1 + arr2
print("Merged array using '+':", merged1)

# Method 2: Using extend()
arr3 = arr1.copy()
arr3.extend(arr2)
print("Merged array using extend():", arr3)



# output:
# Merged array using '+': [10, 20, 30, 40, 50, 60]
# Merged array using extend(): [10, 20, 30, 40, 50, 60]
