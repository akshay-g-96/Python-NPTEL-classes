import math

def isprimebad(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n))):
      if n%i == 0:
         return(False)
    return(True)

def lexsortbad(l):
  for k in range(2):
    for j in range(len(l)-1):
      for i in range(len(l)-1):
        if l[i][k] > l[i+1][k]:
          (l[i],l[i+1]) = (l[i+1],l[i])
  return(l)

def patternprint():
  #content=input()
  #pattern=content.readline()
  
  #if content.find(pattern,0,len(content)):
  #    print (content)
  inp=input()
  while inp!="\n\n":
      inp=input()
      

      
  pattern=inp[0]
  for line in inp:
      if inp.find(pattern):
          print (line)
