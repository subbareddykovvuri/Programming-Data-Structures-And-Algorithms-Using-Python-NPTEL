def repeated(l):
  d={}
  for i in range(len(l)):
    if l[i] not in d:
      d[l[i]]=1
    else:
      d[l[i]]+=1
  count=0
  for c in d:
    if d[c]>1:
      count+=1
  return(count)
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "repeated":
  arg = tolist(farg)
  print(repeated(arg))

