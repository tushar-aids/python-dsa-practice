# Count frequency of each element in an array

nums = [10, 20, 10, 30, 20, 10, 40]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of each element:")
for key in freq:
    print(f"{key} => {freq[key]}")



# output:
# Frequency of each element:
# 10 => 3
# 20 => 2
# 30 => 1
# 40 => 1
