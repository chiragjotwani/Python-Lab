num=int(input("Enter number: "))
sum=0
i=1

for i in range(1,num):
    if (num % i == 0):
        sum= sum+i
        
if(sum==num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")         