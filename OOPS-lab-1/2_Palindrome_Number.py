num=int(input("Enter Number: "))
reverse=0
num1=num

while(num!=0):
    rem=num%10
    reverse=reverse*10 + rem
    num= num//10
    
if(reverse==num1):
    print("palindrome number")
else:
    print("Not palindrome")