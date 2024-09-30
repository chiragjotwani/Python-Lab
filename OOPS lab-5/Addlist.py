enter1= input("Enter 3 integers separated by sapces: ")
list1= list(map(int, enter1.split()))

enter2= input("Enter 3 integers separated by sapces: ")
list2= list(map(int, enter2.split()))

enter3= input("Enter 3 integers separated by sapces: ")
list3= list(map(int, enter3.split()))

result =list(map(lambda x,y,z: x+y+z, list1, list2, list3))

print("Sum of corresponding elemets: ", result)
