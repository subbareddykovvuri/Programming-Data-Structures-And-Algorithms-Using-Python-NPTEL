def expanding(l):
  a=[]
  for i in range(len(l)-1):
    if(l[i+1]>l[i]):
      x=l[i+1]-l[i]
      a.append(x)
    else:
      x=l[i]-l[i+1]
      a.append(x)
  for i in range(0,len(a)-1):
    if(a[i+1]>a[i]):
      if(i+2==len(a)):
        y="True"
        break
    else:
      y="False"
      break
  return y  
  
def accordian(l):
  a=[]
  for i in range(len(l)-1):
    if(l[i+1]>l[i]):
      x=l[i+1]-l[i]
      a.append(x)
    else:
      x=l[i]-l[i+1]
      a.append(x)
  if(len(a)==2):
    if(a[0]==a[1]):
      y="False"
    else:
      y="True"
  if(len(a)>2):
    for i in range(len(a)-2):
      if(a[i]>a[i+1]<a[i+2] or a[i]<a[i+1]>a[i+2]):
        if(i==len(a)-3):
          y="True"
      else:
        y="False"
  return y
      
def rotate(l):
  n=len(l)
  m=[]
  x=[]
  for i in range(n):
    for j in range(n-1,-1,-1):
      x.append(l[j][i])
    m.append(x)
    x=[]
  return m
  

      
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "expanding":
  arg = parse(farg)
  print(expanding(arg))

if fname == "accordian":
  arg = parse(farg)
  print(accordian(arg))

if fname == "rotate":
  arg = parse(farg)
  savearg = []
  for row in arg:
    savearg.append(row[:])
  ans = rotate(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")

