myinput='''
[64,55,64,37,11]
'''

def mergebad(l1,l2):

  (lmerged,i,j) = ([],0,0)

  while i+j < len(l1) + len(l2):
    if i == len(l1):
      lmerged.append(l2[j])
      j = j+1
    elif j == len(l2):
      lmerged.append(l1[i])
      i = i+1
    elif l1[i] < l2[j]:
      lmerged.append(l1[i])
      i = i+1
    elif l2[j] < l1[i]:
      lmerged.append(l2[j])
      j = j+1
    else:
      lmerged.append(l1[i])
      i = i+1
      j = j+1
    
  return(lmerged)    

def mergesortbad(l):
  if len(l) < 2:
    return(l)
  else:
    n = len(l)
    leftsorted = mergesortbad(l[:n//2])
    rightsorted = mergesortbad(l[n//2:])
    return(mergebad(leftsorted,rightsorted))
    

def mergegood(l1,l2):

  (lmerged,i,j) = ([],0,0)

  while i+j < len(l1) + len(l2):
    if i == len(l1):
      lmerged.append(l2[j])
      j = j+1
    elif j == len(l2):
      lmerged.append(l1[i])
      i = i+1
    elif l1[i] <= l2[j]:
      lmerged.append(l1[i])
      i = i+1
    elif l2[j] < l1[i]:
      lmerged.append(l2[j])
      j = j+1

  return(lmerged)    

def mergesortgood(l):
  if len(l) < 2:
    return(l)
  else:
    n = len(l)
    leftsorted = mergesortgood(l[:n//2])
    rightsorted = mergesortgood(l[n//2:])
    return(mergegood(leftsorted,rightsorted))

import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
    print(mergesortbad(myarg) != mergesortgood(myarg))
  except:
    print(False)
