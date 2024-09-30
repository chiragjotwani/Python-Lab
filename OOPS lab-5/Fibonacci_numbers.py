def fibonacci(n):
    sequence=[0,1]
    for i in range(2,n):
        sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[:n]
    
def sq_fibonacci(n):
    fib_numbers=fibonacci(n)
    squared=list(map(lambda x: x**2, fib_numbers))
    return squared

n= int(input("Enter the number of fibonacci numbers: "))

result=sq_fibonacci(n)
print("Square of first", n, "Fibonacci numbers are:", result)
