# Count number of even and odd elements in the array

nums = [12, 7, 9, 20, 33, 14, 5]

even_count = 0
odd_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)



# output:
# Total even numbers: 3
# Total odd numbers: 4

