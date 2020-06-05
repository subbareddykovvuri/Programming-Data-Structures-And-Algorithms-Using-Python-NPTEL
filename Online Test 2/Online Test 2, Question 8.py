def maxaverage(l):
  d={}
  for (name,score) in l:
    if name not in d:
      d[name]=score
    else:
      d[name]=(d[name]+score)/2
  play=[i for i in d if d[i]==max(d.values())]
  return sorted(play)
  
  
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "maxaverage":
  arg = tolist(farg)
  print(maxaverage(arg))
