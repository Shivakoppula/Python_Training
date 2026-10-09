import re

fobj = open('r1.log','r')
for var in fobj:
    var = var.strip()
    if(re.search("^$",var)):
        continue # ignore empty lines
    else:
        print(var) # display non-empty lines