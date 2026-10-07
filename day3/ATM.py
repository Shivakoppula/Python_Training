import time

def pin_test(arg):
    pin = 1234
    if(int(arg) == pin):
        return 1
    

for var in range(3):
    p = input('Enter a pin Number:')
    if(pin_test(p)):
        print(f'Success - input pin is matched entry date/time: {time.ctime()}')
        break
    else:
        print(f'Sorry input pin number is not matched: date/time: {time.ctime()}')
    

if(var >2):
    print(f'pin is blocked - date/time:{time.ctime()}')