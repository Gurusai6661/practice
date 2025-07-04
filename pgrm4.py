# rotating the array clock wise
def rotateArr( arr, d):
        #Your code here
        
    n=len(arr)
    if(d>n):
            
        d %=n
    temp=[0]*n
    for i in range(n-d):
        temp[i]=arr[d+i]
    for i in range(d):
        temp[n-d+i]=arr[i]
    for i in range(n):
        arr[i]=temp[i]
    return arr[i]   
arr=list(map(int, input("Enter elements: ").split()))
d=int(input("enter the rotation:" ))
rotateArr(arr, d)
print (arr)
