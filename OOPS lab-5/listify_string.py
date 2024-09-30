input= input("Enter a list of stirngs separated by spaces:")
strings= input.split()
listified= list(map(list, strings))

print("Listified strings: ", listified)