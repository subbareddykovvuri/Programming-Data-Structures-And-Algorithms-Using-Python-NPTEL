myinput = '''
[(2,5),(6,4)]
'''

def lexsortbad(l):
  for k in range(2):
    for j in range(len(l)-1):
      for i in range(len(l)-1):
        if l[i][k] > l[i+1][k]:
          (l[i],l[i+1]) = (l[i+1],l[i])
  return(l)
    
    
import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(lexsortbad(myarg[:]) != sorted(myarg[:]))
  except:
     print(False)
