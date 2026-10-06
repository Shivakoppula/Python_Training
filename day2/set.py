'''collection based of  unordered unique elements

not index based
not key and value pairs
supports mathematical set operations like union, intersection, difference
can be created using curly braces {} or the set() function
hold null values
'''



s={2,1,1,1,3,3,4,4,5,5,5}
print(s)
s.add(6)
print(s)
s.remove(3)
print(list(s))



print(len(s))







s1={1,2,3,4,5,6}
s2={2,3,6,7,8,9,10}

#union we usee symbol | combine two sets
print(s1 | s2)
print(s1.union(s2))


#intersection we use symbol & common in both 
print(s1 & s2)
print(s1.intersection(s2))

#difference we use symbol - elements in s1 but not in s2
print(s1 - s2)
print(s1.difference(s2))


#symmetric difference we use symbol ^ elements in s1 or s2 but not in both
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
