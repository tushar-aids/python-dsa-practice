# Remove an element from the array

nums = [10, 20, 30, 40, 50]

element = int(input("Enter the element to remove: "))

if element in nums:
    nums.remove(element)
    print("Array after removal:", nums)
else:
    print("Element not found in array.")




# output:
# Enter the element to remove: 30  
# Array after removal: [10, 20, 40, 50]
