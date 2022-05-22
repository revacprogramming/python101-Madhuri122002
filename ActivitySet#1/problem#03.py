# This first line is provided for you
def input(hrs,rate):
  hrs = input("Enter Hours:")
  rate=input("enter rate ")
  return hrs, rate

def compute(hrs,rate):
  pay=hrs*rate
  return pay

hrs=None
rate=None
input(hrs,rate)
pay=compute(hrs,rate)