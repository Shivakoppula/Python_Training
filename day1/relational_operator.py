login_status = input("enter emp login status:")
loged = input("enter emp logined or not:")

if login_status == loged:
    print("welcome")
    print("employee is present")
    
else:
    print("welcome")
    print("employee is absent")

print(f'''Login Status: {login_status}
Logged In: {loged}''')
