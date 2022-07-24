#program 3

def get_cs():
   string=input("Enter a string: ")
   return string

def cs_to_lot(cs):
   lot=cs.split()
   return lot

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)

__name__=input("Enter the name: ")
if __name__ == '__main__':
    main()
