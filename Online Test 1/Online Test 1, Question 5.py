def sumofsquares(n):
  l=[]
  a=int(n**(1/2))
  b=int(a/2)
  for i in range(b,2*a):
    for j in range(b,2*a):
      if i**2+j**2==n:
        return True
      else:
        if j==2*a-1 and i==2*a-1:
          return False
        
import ast

def toint(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "sumofsquares":
  arg = toint(farg)
  print(sumofsquares(arg))

