# Find duplicate elements in an array

nums = [10, 20, 10, 30, 20, 40, 30, 50]

duplicates = []
seen = set()

for num in nums:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.add(num)

print("Duplicate elements are:", duplicates)



# output:
# Duplicate elements are: [10, 20, 30]
