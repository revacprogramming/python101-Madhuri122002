
def add(a, b):
    pass  # ...


def output(a, b, sum):
    pass  # ...

def input_two_numbers():
  a=float(input("Enter a number: "))
  b=float(input("Enter a number: "))
  return a,b
  
def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


__name__=input("Enter the name: ")
if __name__ == '__main__':
    main()
