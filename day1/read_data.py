'''
python program to read the input of keyboard and display it
 emp name,age,salary,login status
 calculate the salary after 18% tax
 total salary =tax+basic salary
'''



name=input("enter emp name:")
age=input("enter emp age:")
basic_salary=float(input("enter emp salary:"))
tax=basic_salary*0.18
total_salary=tax+basic_salary
login_status=input("enter emp login status:")

print(f'''Name: {name}
  ---------------
    Age: {age}
   ---------------
    Salary: {basic_salary}
   ---------------
    Login Status: {login_status}
---------------
total Salary: {total_salary}
---------------
tax:{tax}
    ''')