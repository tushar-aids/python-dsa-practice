# Find pairs in array with a given sum

nums = [2, 4, 3, 5, 7, 8, 1]
target = 9

print("Pairs with sum", target, "are:")

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"({nums[i]}, {nums[j]})")



# output:
# Pairs with sum 9 are:
# (2, 7)
# (4, 5)
# (8, 1)
