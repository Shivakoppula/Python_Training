'''
create the new file and write
  if file alredy exit--> its override the entire the content
'''




wbj=open("r1.log", "w")
wbj.write("This is a new log file.\n")
wbj.write("Appending another line to the log file.\n")
pname="pB"
pscost=465626.23
wbj.write(f"Product name: {pname}, Product cost: {pscost}\n")
wbj.close()
