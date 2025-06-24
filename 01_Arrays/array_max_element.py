# Find the maximum element in the array

nums = [15, 88, 22, 9, 65, 31]

max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num

print("Maximum element:", max_num)



# output:
# Maximum element: 88
