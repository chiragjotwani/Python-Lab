input1= input("Enter a of integers separated by sapces: ")
list1= list(map(int, input1.split()))

input2= input("Enter a of integers separated by sapces: ")
list2= list(map(int, input2.split()))

add=list(map(lambda x,y: x+y, list1, list2))
difference=list(map(lambda x,y: x-y, list1, list2))

print("Added lists: ". add)
print("Difference between lists: ", difference)
