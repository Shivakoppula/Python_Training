print("Welcome")
print("Test-1")
print("Test-2")
print("Test-3")
try:
    print(Test)
except Exception as eobj:
    print(eobj)
else:
    print("There is no Exception")
finally:
    print("Always running")
    
for var in range(5):
    print(var)
    print("-"*10)

total = 10 + 20
print("Total=",total)
print("End of the line")