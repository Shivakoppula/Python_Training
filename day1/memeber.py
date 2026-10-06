memeber=['falsk','fb','whatup','insta']
appname=input("Enter the app name: ")
portnumber=0
if appname in memeber:
    portnumber=5000
elif appname == 'insta':
    portnumber=6000
elif appname == 'fb':
    portnumber=7000
else:
    print(f'{appname} is not available')




print(f'{appname} is available on port {portnumber}')