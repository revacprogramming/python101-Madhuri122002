fname=input("enter the file name:")
fn=open(fname)
count=None
for line in fn:
    if line.startswith("From"):
        lst=line.split()
        count=count+1
        print(lst[1])
        lst.clear()
        
print("there were "+count+" lines in the file with From as the first word")