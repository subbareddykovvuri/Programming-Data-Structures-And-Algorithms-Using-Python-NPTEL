def perfect(n):
  sum1 = 0
  for i in range(1, n):
      if(n % i == 0):
          sum1 = sum1 + i
  if (sum1 == n):
      return(True)
  else:
      return(False)
import ast

def toint(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "perfect":
  arg = toint(farg)
  print(perfect(arg))

