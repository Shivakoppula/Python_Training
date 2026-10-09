'''class InvalidFileError(Exception):
	pass


try:
	raise InvalidFileError("Invalid file")
except InvalidFileError as e:
	print(f"Caught error: {e}")
'''



try:
    n=int(input("Enter a number: "))
    if(n>100):
        raise ValueError("Number is greater than 100")

except Exception as e:
    print(f"Caught error: {e}")


class InsufficientFundsError(Exception):
    pass

balance=1000
withdrawal=int(input("Enter withdrawal amount: "))
try:
    if  withdrawal > balance:
        raise InsufficientFundsError("Insufficient funds")
except InsufficientFundsError as e:
    print(f"Caught error: {e}")
