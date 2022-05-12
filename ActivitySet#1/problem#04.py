hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if h<=40:
    print(h*r)
if h>40:
    print((h*r)*1.5)