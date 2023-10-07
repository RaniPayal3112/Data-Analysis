# Define a list of numbers
numbers = [5, 2, 9, 1, 5, 6]

# Sort the list in ascending order
numbers.sort()

# Calculate the median
n = len(numbers)
if n % 2 == 0:
    # If the number of elements is even, take the average of the middle two elements
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    # If the number of elements is odd, the median is the middle element
    median = numbers[n // 2]

# Print the median
print("Median:", median)






