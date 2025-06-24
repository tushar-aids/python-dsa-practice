# Right rotate an array by 1 position

nums = [10, 20, 30, 40, 50]

last = nums[-1]

for i in range(len(nums)-1, 0, -1):
    nums[i] = nums[i - 1]

nums[0] = last

print("Array after right rotation:", nums)



# output:
# Array after right rotation: [50, 10, 20, 30, 40]
