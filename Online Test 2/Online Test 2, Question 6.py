def intersect(l1,l2):
  l=[]
  for i in l1:
    if i in l2 and i not in l:
      l.append(i)
  return l
import ast

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intersect":
   (arg1,arg2) = topairoflists(farg)
   print(intersect(arg1,arg2))
