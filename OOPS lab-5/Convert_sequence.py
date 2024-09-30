sequence= input("Enter a sequence of characters: ")
unique=''.join(set(sequence ))
result= list(map(str.upper,[unique])) +list(map(str.lower, [unique]))

print("Uppercase: ", result[0])
print("Lowercase: ", result[1])