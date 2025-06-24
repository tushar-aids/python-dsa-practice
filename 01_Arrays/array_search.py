# Linear search in an array

nums = [10, 20, 30, 40, 50]
key = int(input("Enter the number to search: "))

found = False
for i in range(len(nums)):
    if nums[i] == key:
        print(f"{key} found at index {i}")
        found = True
        break

if not found:
    print(f"{key} not found in the array")



# output:
# Enter the number to search: 30
# 30 found at index 2
# or
# Enter the number to search: 99
# 99 not found in the array
