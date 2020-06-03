myinput='''
(2,1,3)
'''

def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)

def max3good(x,y,z):
  if x >= y and x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)

import ast

try:
   (myarg1,myarg2,myarg3) =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
    print(max3bad(myarg1,myarg2,myarg3) != max3good(myarg1,myarg2,myarg3))
  except:
    print(False)
