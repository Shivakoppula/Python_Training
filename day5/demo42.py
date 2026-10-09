import sys

try:
    fobj = open('invalidFile','r')
except PermissionError as eobj:
    print("This is 1st Except block")
    print(eobj)
except FileNotFoundError as eobj:
    print("This is 2n Exception block")
    print(eobj)

# Vs
try:
    fobj = open('InvalidFile','r')
except Exception as eobj:
    print(eobj)

print("") # empty line    
# Vs 
try:
    fobj = open('InvalidFile','r')
except Exception:
    print(sys.exc_info())