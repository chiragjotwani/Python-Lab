input= input("Enter a of integers separated by sapces: ")
numbers= list(map(int, input.split()))

squared= list(map(lambda x: x**2, numbers))

print("Squared numbers: ", squared)
