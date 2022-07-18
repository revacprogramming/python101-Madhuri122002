

def get_cs():
  inp=input('enter a string:')
  return inp

def cs_to_dict(cs):
  counts=dict()
  lst=cs.split()
  for words in lst:
    counts[words]=counts.get(words,0)+1
  return counts

def dict_to_cs(d):
  string=""
  for i in d:
    string=string+i
  return string
  
def main():
  cs = get_cs()
  d = cs_to_dict(cs) # convert connect string to a dictionary
  print(d)

  cs = dict_to_cs(d)
  print(cs)

__name__=input("Enter the file name: ")
if __name__ == '__main__':
    main()
