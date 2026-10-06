list_tuple = [1, (2, 3), 4]
tuple_list = (5, [6, 7], 8)

print("Nested list with tuple:")
for item in list_tuple:
	print(item)

print("Tuple inside the list:")
for item in list_tuple[1]:
	print(item)

print("Tuple with nested list:")
for item in tuple_list:
	print(item)

print("List inside the tuple:")
for item in tuple_list[1]:
	print(item)
