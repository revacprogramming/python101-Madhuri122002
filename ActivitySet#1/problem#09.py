fname=input("enter the file name:")
fn=open(fname)
lst=list()
for line in fn:
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append()
            
lst.sort()
print(lst)