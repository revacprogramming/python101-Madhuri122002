fname=input("Enter the file name:")
fn=open(fname)

count=0
for line in fn:
    if line.startswith("From"):
        words=line.split()
        count+=1
        print(words[1])
        words.clear()

print(count)