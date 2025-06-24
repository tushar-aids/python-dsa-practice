# Separate even and odd numbers from an array

nums = [12, 7, 9, 20, 33, 14, 5]

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)



# output:
# Even numbers: [12, 20, 14]
# Odd numbers: [7, 9, 33, 5]
