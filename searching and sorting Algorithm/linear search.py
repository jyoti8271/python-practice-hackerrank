def linear_search(arr,target):
    size=len(arr)
    for index in range (0,size):
        if arr[index]==target:
            return index
        
    return -1
    
arr=list(map(int,input("enter the numbers").split()))

target=int(input("Enter the target:"))
result=linear_search(arr,target)
print(result)
    
        