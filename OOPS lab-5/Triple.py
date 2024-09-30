def triple(n):
    return n*3
input= input("Enter a of integers separated by sapces: ")
numbers= list(map(int, input.split()))

tripled=list(map(triple, numbers ))
print("tripled numbers are: ", tripled)