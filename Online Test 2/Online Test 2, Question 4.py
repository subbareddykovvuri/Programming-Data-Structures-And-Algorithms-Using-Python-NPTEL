def oddpositions(l):
  if len(l) <= 1:
    return([])
  else:
    return(
       # Complete the recursive call below this line
l[1::2]
       # Complete the recursive call above this line
    )

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "oddpositions":
  arg = tolist(farg)
  print(oddpositions(arg))
