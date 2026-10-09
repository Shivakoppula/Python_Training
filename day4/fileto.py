fobj=open("C:\\Users\\Admin\\Documents\\emp.csv", "r")
l=fobj.readlines()
fobj.close()
total=0
for var in l:
    if 'sales' in var:
        var=var.strip()
        emp=var.split(",")
        cost=emp[-1]
        total=total+int(cost)
print(total)