menu = int(input("Enter your choice: \n  1.Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n"))

num1= int(input("Enter number:"))
num2= int(input("Enter number:"))
          
if (menu==1):
    print(num1+num2)

elif (menu==2):
    print(num2-num1)

elif(menu==3):
    print(num1*num2)

else:
    print(num2/num1)