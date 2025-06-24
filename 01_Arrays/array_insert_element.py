# Insert an element at a specific position in the array

nums = [10, 20, 30, 40, 50]

element = int(input("Enter the element to insert: "))
position = int(input("Enter the position (0-based index): "))

if position < 0 or position > len(nums):
    print("Invalid position!")
else:
    nums.insert(position, element)
    print("Array after insertion:", nums)



# output:
# Enter the element to insert: 25  
# Enter the position (0-based index): 2  
# Array after insertion: [10, 20, 25, 30, 40, 50]
