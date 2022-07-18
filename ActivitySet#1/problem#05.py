def inp():
  hrs=float(input("enter the hours:"))
  rate=float(input("enter the rate:"))
  return hrs,rate

def computepay(h,r):
  if h<=40:
      return (h*r)
  if h>40:
      return ((40*r)+((h-40)*1.5*r))

def output(pay):
  print("Pay: ",pay)

h,r=inp()
pay=computepay(hrs,rate)
output(pay)