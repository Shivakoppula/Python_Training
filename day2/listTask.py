'''
python program
create empty list
display number of elements in list # use len() function-->0

loop operation by while limit is 5
a--> read a hostname from user input
b--> append the hostname to the list
display the number of elements in the list # use len() function-->5

use for loop -iterate through the list


read a hostname from user input user input

test input hostname is exist or not in list
 if exist modify hostname(last index) 
 if not exist add hostname to list

'''

'''
host = []

print(f'Number of elements:{len(host)}')#length 0

i = 0
while i < 5:
	hostname = input("Enter hostname: ")
	host.append(hostname)
	i += 1

print(f'Number of elements:{len(host)}')#length 5

for ele in host:
	print(ele)

new = input("Enter hostname to test: ")

if new in host:
	host[-1] = new
	print("Hostname exists. Last item modified.")
else:
	host.append(new)
	print("Hostname not found. Added to list.")

print(f'Updated list:{host}')

print('\n')

for ele in host:
     print(ele)'''
     
     
     
'''
given list
emp=['101,shiva,apprentice,2000','102,robbin,ceo,4000','103,venkat,manager,2500','104,veera,mentor,2200']
    iterate the list
    split each element by using  comma
    display the emp nam in title case and emp depart name in uppercase
    calculate the total salary of all employees and display it
    calculate the total salary of all apprentices and display it
     '''
     
total_salary = 0
salary=0
emp=['101,shiva,apprentice,2000','102,robbin,APPRENTICE,4000','103,venkat,manager,2500','104,veera,mentor,2200']
for e in emp:
    emp_data = e.split(',')
    #print(emp_data)
    emp_name = emp_data[1].title()
    emp_dept = emp_data[2].upper()
    # check if the employee is an apprentice
    if emp_dept=='APPRENTICE':
        emp_salary = int(emp_data[3])
        salary+= emp_salary
        print(f'APPRENTICEs total Salary: {salary}')
    emp_salary = int(emp_data[3])
    total_salary += emp_salary
    print(f'Name: {emp_name}, Department: {emp_dept}')
print(f'Total Salary: {total_salary}')





     

