

hrs=float(input("enter the hours:"))
rate=float(input("enter the rate:"))

def computepay(h,r):
  if h<=40:
      return (h*r)
  if h>40:
      return ((40*r)+((h-40)*1.5*r))

pay=computepay(hrs,rate)
print("Pay",pay)