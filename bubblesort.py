
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,1,3,5,6,9,4]
res=bubblesort(arr)
print(res)