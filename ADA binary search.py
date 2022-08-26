def binary(arr,l,key,h):
    
    if(h>=l):
        mid=(l+h)//2
    if(arr[mid]==key):
        return mid
    else:
        if(arr[mid]>key):
            return binary(arr,l,key,mid-1)
        else:
            return binary(arr,mid+1,key,h)                          

arr=[1,3,14, 9,45,65,88]
key=65
print("The key value is present at", binary(arr,0,key,len(arr)-1))