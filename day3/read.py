fobj=open('C:\\Users\\Admin\\Documents\\emp.csv','r')
l=fobj.readlines()
fobj.close()




'''for var in l:
    for item in var.split(','):
        if 'sales' in item:
            print(item)
'''

total=0
for var in l:
    if 'sales'in var:
        var=var.strip()
        eid,ename,edept,eplace,ecost=var.split(',')
        total=total+int(ecost)
        print(f" Emp name is {ename.title()} from {edept.title()} department has sum of sales: {total}")
        
        print(var)