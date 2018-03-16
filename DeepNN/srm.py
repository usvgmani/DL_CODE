import numpy as np 
import itertools as it
def factorial(n):
    return np.prod(range(1,n+1))

def nchoosek(n,k):
    return np.divide(factorial(n),(np.multiply(factorial(k), factorial(n-k))))

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
def choose(l, k):
    return list(choose_iter(l, k))
    
P=1000000000    
def power(a,b):
    ret=1
    while(b>0):            
        if((b&1)==1):
            ret=ret*a%P
        a=a*a%P
        b=b>>1
    return ret
    
def findExp(n,x):    
    ans = power(2,n)
    ways = 1     
    inv = np.zeros(2000000)
    inv[0] = 0 
    inv[1] = 1 
    i=2
    while( i < len(inv)): 
      inv[i] = P - ( (P / i) * np.mod(inv[np.mod(P,i)], P))
      i=i+1
      
    i=0  
    while ( i < x) :
        ans =ans- ways
        if (ans < 0) :
            ans = ans + P
        ways = (ways * np.mod((n - i), P) * np.mod(inv[i + 1], P))
        i=i+1
    return (2*np.mod(ans, P));   

#print ("{} choose {}: {}".format(3, 2,nchoosek(3,2)))


def choosealt(n, x):
  comblst=list(it.combinations(np.arange(1,n+1),x))
  return len(comblst)*np.mean(np.power(2,[min(x) for x in (comblst)]))  
    
#print(choosealt(11,5))


#print(findExp(11,5))
             
def arrij(n):
    arr=np.random.randint(n,size=n)
    print(arr)
    combinationlist=[]
    Max=0
    for j in reversed(range(0,len(arr))):
        for i in range(0,len(arr)): 
            if ((j-i)>Max and arr[j]>arr[i]):
                Max=j-i
                combinationlist=(j,i)
    return combinationlist   

def altarrij(n):
    arr=np.random.randint(n,size=n)
    print(arr)
    L=np.array([])
    L.resize(n)
    R=np.array([])
    R.resize(n)
    L[0]=arr[0]
    for i in range(1,n):
        L[i] =min(arr[i],L[i-1])
    R[n-1]=arr[n-1]    
    for j in range(n-2,-1,-1):
        R[j]=max(R[j+1],arr[j])
    i=0
    j=0
    maxdiff=-1    
    while(i<n and j<n):
        if(L[i]<R[j]):
            prevmax=maxdiff
            maxdiff=max(maxdiff,j-i)
            if(prevmax!=maxdiff):
                print(arr[j],arr[i],j,i)  
            j=j+1
        else:
            i=i+1
    print(maxdiff)    
#print(arrij(10000))
def iarri(n):    
    arr=np.random.randint(n,size=n)
    print(arr)
    singlepos=np.max(np.where(arr==np.max(arr))[0])
    tslice=np.array([])
    tslice.resize(n)
    if(singlepos<n-1):
        i=0
        for val in (arr[singlepos+1:]):
           tslice[i]=val
           i=i+1        
        for val in (arr[:singlepos+1]):
            tslice[i]=val
            i=i+1
        arr=tslice
    print(arr)
    
def sumiarri(n):
    arr=np.random.randint(n,size=n)
    print(arr)
    i=0
    sumarr=0
    currval=0
    for i in range(0,n):
        sumarr = sumarr+arr[i]
        currval=currval+i*arr[i]
    maxval=currval
    print(sumarr)
    for j in range(1,n):        
        currval=currval+sumarr - n*arr[n-j]
        if(currval>maxval):
            maxval=currval
    return maxval
        
#(altarrij(10))

def rearrangeposneg(n):
   # arr=np.random.randint(-n,n,size=n)
    arr=[ 3 ,-7 ,-4 , 8 , 2,  0,-8 ,-7 ,-9 , 3]
    print(arr)
    j=n-1
    k=j
    pos=True
    if(arr[0])<0:
        pos=False
    for i in range(1,n):
        if(not pos and arr[i]<0):#look for positive
            while(not pos and i<=j):
                if(arr[j]>0):
                    pos=True
                    arr[i],arr[j]=arr[j],arr[i]                    
                j=j-1   
                k=j
                    
        elif( pos and arr[i]>=0):#look for negative
            while(pos and i<=j):
                if(arr[j]<0):
                    pos=False
                    arr[i],arr[j]=arr[j],arr[i]                
                j=j-1  
                k=j
        else:
            if(pos and arr[i]>=0 and i<=n-1 and k<=n-1):
                arr[i],arr[k]=arr[k],arr[i]
                k=k+1      
                pos=False
            elif(not pos and arr[i]<0 and i<=n-1 and k<=n-1):
                arr[i],arr[k]=arr[k],arr[i]
                k=k+1    
                pos=True
            else:      
                pos=not pos                    
    return arr
      
print(rearrangeposneg(10))
