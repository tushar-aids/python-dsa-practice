# Left rotate an array by 1 position

nums = [10, 20, 30, 40, 50]

first = nums[0]

for i in range(1, len(nums)):
    nums[i - 1] = nums[i]

nums[-1] = first

print("Array after left rotation:", nums)



# output:
# Array after left rotation: [20, 30, 40, 50, 10]
