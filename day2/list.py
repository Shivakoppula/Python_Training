#list operations
from logging import info


my_list = [1, 2, 3, 4, 5]

#accessing elements
print(my_list[0])  # first element
print(my_list[-1]) # last element

#slicing
print(my_list[1:3]) # elements from index 1 to 2

#adding elements
my_list.append(6)
print(my_list)
my_list.insert(2, 10)
print(my_list)

#removing elements
my_list.remove(3)
print(my_list)
my_list.pop()
print(my_list)

#other operations
print(len(my_list))
print(2 in my_list)
print(my_list)  # final state of the list


#split operation
str="i,am,shiva,koppula,doing,job,in,cisco"
list=str.split(",")
print(list)


#join operation

print(';'.join(list))

print('-'.join(list))



#multiline initialization
'''v1,v2,v3='shiva','koppula','doing'
print(v1)
print(v2)
print(v3)'''

info=['shiva','koppula','doing']
'''name=info[0]
surname=info[1]
activity=info[2]
print(name)
print(surname)
print(activity)'''


name,surname,activity=info
print(name)
print(surname)
print(activity)