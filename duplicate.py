def duplicate(arr):
    n=len(arr)
    if(n==0 or n==1):
        return arr
    else:
        temp=[0]*n
        pivot=0
        for i in range(0,n-1):
            if(arr[i]!=arr[i+1]):
                temp[pivot]=arr[i]
                pivot+=1
        temp[pivot]=arr[n-1]
        return temp[0:pivot+1]
arr=[1,1,2,2,2,3,4,4,4,5,5,5]
res=duplicate(arr)
print(res)
