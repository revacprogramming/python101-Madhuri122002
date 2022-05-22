
def compute(h,r):
  if h<=40:
    return(h*r)
    if h>40:
    return((40*r)+((h-40)*r*1.5))

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
pay=compute(h,r)