list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,10)

strings_from_list = list(map(str, list1))
strings_from_tuple = list(map(str, tuple1))

combined_strings= strings_from_list + strings_from_tuple

print("Combined list of strings: ", combined_strings)
