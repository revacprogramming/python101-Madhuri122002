# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0
search=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count=count+1
        extract=line.strip("X-DSPAM-Confidence:    ")
        num=float(extract)
        add=add+num
    
average=add/count
print("Average spam confidence:",average)