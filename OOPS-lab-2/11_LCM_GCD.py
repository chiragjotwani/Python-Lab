n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
GCD=1
for i in range(2,n1+1):
    if(n1%i==0 and n2%i==0):
        print("GCD of",n1, "and", n2,"is", i)
    
LCM=int((n1*n2)/GCD)
print("LCM of number is: ", LCM)