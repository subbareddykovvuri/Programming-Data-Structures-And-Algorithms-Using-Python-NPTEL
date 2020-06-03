l=[]
while True:
  st=input()
  if st=='':
    break
  else:
    l.append(st)
for i in range(2,len(l),3):
  print(l[i])
