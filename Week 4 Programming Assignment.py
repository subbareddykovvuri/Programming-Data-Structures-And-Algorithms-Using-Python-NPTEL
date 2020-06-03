def frequency(a):
  a.sort()
  i=0
  d={}
  while i<len(a):
    d[a[i]]=a.count(a[i])
    i=i+a.count(a[i])
  maxf=[]
  minf=[]
  for i in d:
    if d[i]==max(d.values()):
      maxf.append(i)
  for i in d:
    if d[i]==min(d.values()):
      minf.append(i)
  maxf.sort()
  minf.sort()
  return(minf,maxf)
def onehop( list):
    mylist=[(a[0],b[1]) for a in list for b in list if a[1]==b[0] and a[0]!=b[1]]
    k=set(mylist)
    rlist=[i for i in k]
    return sorted(rlist)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "frequency":
  arg = parse(farg)
  print(frequency(arg))

if fname == "onehop":
  arg = parse(farg)
  print(onehop(arg))

  

