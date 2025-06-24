# Reversing an array using slicing and loop

# Original array
nums = [10, 20, 30, 40, 50]

# Method 1: Using slicing
rev1 = nums[::-1]
print("Reversed using slicing:", rev1)

# Method 2: Using reverse() function (in-place)
nums2 = nums.copy()
nums2.reverse()
print("Reversed using reverse():", nums2)

# Method 3: Manual method using loop
nums3 = nums.copy()
n = len(nums3)
for i in range(n // 2):
    nums3[i], nums3[n - i - 1] = nums3[n - i - 1], nums3[i]
print("Reversed manually:", nums3)



# output:
# Reversed using slicing: [50, 40, 30, 20, 10]
# Reversed using reverse(): [50, 40, 30, 20, 10]
# Reversed manually: [50, 40, 30, 20, 10]
