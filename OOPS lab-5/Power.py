input= input("Enter a of integers separated by sapces: ")
bases= list(map(int, input.split()))

result= list(map(lambda base, index: base** index, bases, range (len(bases))))

print("Powers based on index: ", result)