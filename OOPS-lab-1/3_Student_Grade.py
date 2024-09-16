percentage=int(input("Enter Percentage of student: "))

if (percentage>90 and percentage<=100):
    print("A+ Grade")

elif(percentage>80 and percentage<=90):
    print("A Grade")

elif(percentage>70 and percentage<=80):
    print("C Grade")

elif(percentage<=70 and percentage>60):
    print("D Grade")

elif(percentage<=60):
    print("E Grade")

else:
    print("Invalid input")