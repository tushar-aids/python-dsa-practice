# Print unique elements from an array

nums = [10, 20, 10, 30, 40, 30, 50, 60]

freq = {}

# Count frequency of each element
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Print elements that appear only once
print("Unique (non-repeating) elements are:")
for key in freq:
    if freq[key] == 1:
        print(key)



# output:
# Unique (non-repeating) elements are:
# 20
# 40
# 50
# 60
