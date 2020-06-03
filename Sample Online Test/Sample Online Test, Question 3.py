def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line
  elif x>=y and x>=z and x>=w:
    maximum=x
  elif y>=x and y>=z and y>=w:
    maximum=y
  elif z>=y and z>=x and z>=w:
    maximum=z
  # Your code above this line
  return(maximum)

import ast

def totripleint(inp):
  inp = "[" + inp + "]"
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "max4":
  arglist = totripleint(farg)
  print(max4(arglist[0],arglist[1],arglist[2],arglist[3]))
  
