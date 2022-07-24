fname=input("Enter the file name: ")
fn=open(fname)
for line in fn:
  if line.startswith("From"):
    f=line.find("s")

print(f)