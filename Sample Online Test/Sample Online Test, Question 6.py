def sublist(l1,l2):
  for i in range(len(l2)-len(l1)+1):
    if l2[i:len(l1)+i]==l1:
      return True
  return False
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

if fname == "sublist":
   (arg1,arg2) = topairoflists(farg)
   print(sublist(arg1,arg2))
