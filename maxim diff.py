def maxi(arr):
    arr.sort()
    n=len(arr)
    maxim=-9999*999

    for i in range(n-1):
        if(arr[i+1]-arr[i]>maxim):
            maxim=arr[i+1]-arr[i]
    return maxim
arr=[5,32,45,4,12,18,25]
res=maxi(arr)
print("the maximum difference is:",res)