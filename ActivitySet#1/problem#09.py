fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst1=line.split()
    for word in lst1:
        if word in lst:
            continue
        else:
            lst.append(word)
            
print(lst.sort())
