def binary_search(arr,n):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==n:
            return True
        elif arr[mid]<n:
            l=mid+1
        else:
            r=mid-1
    return False

arr,n=[1,2,3,4,5],6
result=binary_search(arr,n)
print("The number {} is {} in the given array.".format(n, 'present' if result else 'not present'))
