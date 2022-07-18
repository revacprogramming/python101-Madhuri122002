# This first line is provided for you
def inp():
  hrs = float(input("Enter Hours:"))
  rate=float(input("enter rate "))
  return hrs, rate

def compute(val):
  return val[0]*val[1]

def output(pay):
  print(pay)
  
val=inp()
pay=compute(val)
output(pay)