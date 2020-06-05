def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
    # Your code below this line
    l.sort()
    mythirdmin=l[2]
    # Your code above this line
  return(mythirdmin)

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "thirdmin":
  arg = tolist(farg)
  print(thirdmin(arg))
  
