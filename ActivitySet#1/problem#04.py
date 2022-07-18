def inp():
  hrs = float(input("Enter Hours:"))
  rate=float(input("enter rate:"))
  return hrs,rate
  
def compute(val):
  if val[0]<=40:
    return(val[0]*val[1])
  if val[0]>40:
    return((40*val[1])+((val[0]-40)*val[1]*1.5))

def output(pay):
  print(pay)
  
val=inp()
pay=compute(val)
output(pay)