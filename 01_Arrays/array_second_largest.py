# Find second largest element in an array

nums = [12, 45, 23, 67, 89, 67, 89]

largest = second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest element found.")
else:
    print("Second largest element is:", second)



# output:
# Second largest element is: 67
