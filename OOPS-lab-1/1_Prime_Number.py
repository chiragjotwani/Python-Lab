num1=int(input("Enter number: "))

for i in range(2,num1):
    if(num1%i==0):
        print("Not a prime number")
    else:
        print("prime number")
        break