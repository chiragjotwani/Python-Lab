num = int(input("Enter number: "))
factorial=1

if (num<0):
    print("Invalid input")

elif (num==0):
    print("1")

else:
    for i in range(1, num+1):
        factorial= factorial*i
    print("Factorial of number is", factorial)