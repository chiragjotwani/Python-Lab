n=int(input("Enter number: "))
a = 0
b = 1
i=0
next_number = b

while(i<n):
    print(a, end=" ")
    next_number = a+b
    a,b = b,next_number
    i += 1
    


