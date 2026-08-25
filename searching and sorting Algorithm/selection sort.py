def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index=i
        
        for j in range(i+1,n):
            
            if (arr[j]<arr[min_index]):
                arr[j],arr[min_index]=arr[min_index],arr[j]
                min_index=i
    return arr
            
arr=[10,20,3049,934,923,39,904]
result=selection_sort(arr)
print(result)
                