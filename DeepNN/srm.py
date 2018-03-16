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
            if(pos and arr[i]>=0 and i<=n-1 and k<n):
                while(pos and k<n):
                    if(arr[k]<0):
                        pos=False
                        arr[i],arr[k]=arr[k],arr[i]
                    k=k+1      
            elif(not pos and arr[i]<0 and i<=n-1 and k<n):
                while(not pos and k<n):
                      if(arr[k]>0):
                          pos=True
                          arr[i],arr[k]=arr[k],arr[i]
                      k=k+1 
            else:                   
                pos=not pos                    
    return arr
