'''
This is a task file for DAY-1 training.



python programming exercises.
atm pin validation
limit is 3
limit exceed print "Limit exceeded"
'''


pin=int(input("Enter your ATM pin: "))
count=0
while(count<3):
    if pin==1679:
        print("PIN accepted")
        count=count+1
        break
    else:
        print("Incorrect PIN")
        
        if count==3:
            print("Limit exceeded")
            print("atm blocked try after 24 hours")
            count+=1
    break
       