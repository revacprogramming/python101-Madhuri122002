fname=input("enter a file name: ")
fn=open(fname)
emails=list()
counts=dict()
email=""
for line in fn:
  if line.startswith("From"):
    line=line.split()
    email=line[1]
    emails.append(email)
    counts[email]=counts.get(email,0)+1

maximum=None
maxword=None
for key,val in counts.items():
  if maximum is None or maximum<val
    maximum=val
    maxword=key

print(maxword," ",maximum)