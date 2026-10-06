'''
python prohgram
    create empty dic
    display no elements
    use while loop limit 5
    read hostname from elements
    read IP address from elements
    add input details hostname and ip to an existing dict
    dictname(new key) = new value
display no od items

use for loop
 display dictionary items
 
 read hostname from stdin
 test input hostname is exist update ip 127.0.0.1
 
 if not create new host 127.0.0.1
 display update dict details

'''




lap={}
print("Number of elements:", len(lap))
i=0
while i<5:
    hostname=input("enter the hostname: ")
    ip=input("enter the IP address")
    lap[hostname]=ip
    i+=1


lap["host6"] = "127.0.0.6"
print("Number of elements after input:", len(lap))
for hostname, ip in lap.items():
    print(f"Hostname: {hostname}, IP: {ip}")
 

h=input("enter the hostname to update")   
if h in lap:
    lap[h] = "127.0.0.1"
else:
    lap[h] = "127.0.0.1"

print("Updated dictionary details:")
for hostname, ip in lap.items():
    print(f"Hostname: {hostname}, IP: {ip}")