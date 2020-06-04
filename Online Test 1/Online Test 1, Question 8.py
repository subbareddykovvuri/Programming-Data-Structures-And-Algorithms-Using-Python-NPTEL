def maxaggregate(l):
  d={}
  for (name,score) in l:
    if name not in d:
      d[name]=0
    d[name]+=score
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

if fname == "maxaggregate":
  arg = tolist(farg)
  print(maxaggregate(arg))
