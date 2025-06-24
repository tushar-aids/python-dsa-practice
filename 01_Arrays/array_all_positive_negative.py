# Separate positive and negative numbers in an array

nums = [12, -7, 5, -3, 0, -15, 8, 4]

positive = []
negative = []

for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)



# output:
# Positive numbers: [12, 5, 0, 8, 4]
# Negative numbers: [-7, -3, -15]
