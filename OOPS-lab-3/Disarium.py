x=int(input("enter a number "))
count=0
temp=x
temp2=x
sum=0
while(x>0):
    ld=x%10
    count+=1
    x=x//10
while(temp2>0):
    ld=temp2%10
    sum=sum+ld**count
    count-=1
    temp2=temp2//10
if(sum==temp):
    print("Disarium Number")
else:
    print("Not Disarium Number")