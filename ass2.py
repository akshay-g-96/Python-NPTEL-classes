def intreverse(n):
    rev=0
    while n>0:
        rev=(10*rev) + n%10
        n//=10
    return rev

def matched(s):
    i=0
   # length=len(s)
    for j in s:
        if i <= -1  :
            break
        if j == "(" :
            i+=1
        if j == ")" :
            i-=1
    if i==0 :
        return True
    else :
        return False
        

def sumprimes(l):
    s=0
    f=0
    z=len(l)
    for i in l:
        #j=0
        for j in range (2,i,1):
            if(i%j==0):
                break
            f=+1
        if(f==i-2):
            s=s+i
       # s=s+i
    return s
            
        
    
