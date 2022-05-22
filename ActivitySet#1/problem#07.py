def num():
  text = "X-DSPAM-Confidence:    0.8475"
  t=text.find(":")
  stext=text.strip("X-DSPAM-Confidence:")
  s=float(stext)
  return s

s=num()
print(s)