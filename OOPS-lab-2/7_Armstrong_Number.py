num = int(input("Enter number: "))
temporary = num
order = len(str(num))
sum=0

while (temporary>0):
    remainder= temporary % 10
    sum= sum + (remainder**order)
    temporary= temporary//10
    
if(num==sum):
    print(num,"is Armstrong number")
else:
    print(num, "is not Armstrong number")
    