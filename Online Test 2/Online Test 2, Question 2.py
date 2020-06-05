myinput = '''
[(3,5),(6,5),(3,5)]
'''

def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
def stablesortgood(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] > l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(stablesortbad(myarg[:]) != stablesortgood(myarg[:]))
  except:
     print(False)
