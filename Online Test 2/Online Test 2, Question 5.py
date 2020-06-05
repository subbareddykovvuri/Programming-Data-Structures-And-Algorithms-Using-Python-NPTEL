def sumof3squares(n):
  a=int(n**(1/3))
  b=int(a/2)
  for i in range(b,2*a):
    for j in range(b,2*a):
      for k in range(b,2*a):
        if i**2+j**2+k**2==n:
          return True
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

if fname == "sumof3squares":
  arg = toint(farg)
  print(sumof3squares(arg))

