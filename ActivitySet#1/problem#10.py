fname=input("enter a file name: ")
fn=open(fname)
emails=list()
counts=dict()
email=""
for line in fn:
  if line.startswith("From"):
    line=line.split()
    email=line[1]
    counts[email]=counts.get(email,0)+1

for 