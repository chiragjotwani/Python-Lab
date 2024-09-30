input=input("Enter list of integers separated by spaces: ")
numbers = list(map(int, input.split()))

sum = sum(numbers)
print("Sum of elements in the array:", sum)