def inp():
  score=float(input("Enter the score"))
  return score

def compute(score):
  if score>=0.9:
    return "A"
  elif score>=0.8:
    return "B"
  elif score>=0.7:
    return "C"
  elif score>=0.6:
    return "D"
  elif score<0.6:
    return "F"
  else:
    return "error"

def output(grade,score):
  print("the score obtained is ",score," and the corresponding grade is ",grade)

score=inp()
grade=compute(score)
output(grade,score)