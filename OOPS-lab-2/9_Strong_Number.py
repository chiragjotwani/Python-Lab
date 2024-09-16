num= int(input("Enter number: "))
sum=0

temporary= num


while(num>0):
    i=1
    factorial=1
    remainder = temporary % 10
    
    while(i<remainder+1):
        factorial= factorial*i
        i+=1
sum= sum+factorial
temporary= temporary//10
    
if(sum==num):
    print(num, "is a strong number")
    
else:
    print(num,"is not a strong number")
