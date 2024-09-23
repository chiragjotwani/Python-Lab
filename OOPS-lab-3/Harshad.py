x=int(input("enter a number "))
temp=x
sum=0
while(x>0):
    ld=x%10
    sum+=ld
    x=x//10
if(temp%sum==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")    