# Taking array input from user using loop

n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    nums.append(val)

print("You entered:", nums)

# Sum and Average
total = sum(nums)
average = total / n

print("Sum =", total)
print("Average =", average)



# output:
# Enter number of elements: 5
# Enter element 1: 10
# Enter element 2: 20
# Enter element 3: 30
# Enter element 4: 40
# Enter element 5: 50
# You entered: [10, 20, 30, 40, 50]
# Sum = 150
# Average = 30.0
