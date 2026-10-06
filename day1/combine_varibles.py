dept="IT"
# combining the strings with named varible

# way-1 by using seperaor ','
print("I am working in the dept :", dept)

#way -2 using extend fromat
print("I am working in the dept is: %s" %dept)


#way-3 by using {} format
print("I am working in the dept : {}".format(dept))



#most recommended way and preferalbe
#way-4 by using f-strings (formatted string literals)
print(f"I am working in the dept : {dept}")

# way-5 by using concatenation with '+'
print("I am working in the dept :"+ dept)


print("----------------------------------------------------")


'''

program to demonstrate to inistailize the employee details(name,age,salary,login status)



Excepted output:
emp name:shiva
emp age:30
emp salary:50000
emp login status:True
'''



name="shiva"
age=30
salary=50000
login_status=True
print(f'emp name:{name}')
print(f'emp age:{age}')
print(f'emp salary:{salary}')
print(f'emp login status:{login_status}')


