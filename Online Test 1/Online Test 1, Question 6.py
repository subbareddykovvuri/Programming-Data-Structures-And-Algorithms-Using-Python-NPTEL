def subsequence(l1,l2):
  for i in l1:
    if i in l2:
      l2=l2[l2.index(i)+1:len(l2)]
    else:
      return False
    
  return True
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

if fname == "subsequence":
   (arg1,arg2) = topairoflists(farg)
   print(subsequence(arg1,arg2))
