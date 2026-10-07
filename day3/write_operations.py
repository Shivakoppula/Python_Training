fbj=open('r1.log','r')
wbj=open('r1.log','w')


s=fbj.read()
wbj.write(s)

fbj.close()
wbj.close()


with open('r1.log','r') as fbj:
    with open('r1.log','w') as wbj:
        s=fbj.readlines()
        for var in s:
            wbj.write(f'data->{var}')
            
            
            
            
print("Write operation completed.")