myinput = '''
4
'''

import math

def isprimebad(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n))):
      if n%i == 0:
         return(False)
    return(True)

def isprimegood(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n)+1)):
      if n%i == 0:
         return(False)
    return(True)




import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(isprimebad(myarg) != isprimegood(myarg))
  except:
     print(False)
