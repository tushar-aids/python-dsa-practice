# Find the minimum element in the array

nums = [15, 88, 22, 9, 65, 31]

min_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num

print("Minimum element:", min_num)



# output:
# Minimum element: 9
