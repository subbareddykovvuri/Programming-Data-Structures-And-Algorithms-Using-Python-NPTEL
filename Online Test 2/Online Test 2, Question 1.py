myinput = '''
[-6,-7,-8,-10]
'''

def maxbad(l):
  mymax = 0
  for i in range(len(l)):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)

import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(maxbad(myarg) != max(myarg))
  except:
     print(False)
