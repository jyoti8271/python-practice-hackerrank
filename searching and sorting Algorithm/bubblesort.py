# def bubble_sort(arr):
#     n=len(arr)
#     for passes in range(0,n):
#         for j in range(0,n-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
                
#     return arr
# arr=list(map(int,input("enter the number:").split()))
# result=bubble_sort(arr)
# print("sorted result",result)





#already sorted element ko bar bar sort nhi krega
def bubble_sort(arr):
    n=len(arr)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr
arr=list(map(int,input("enter the number:").split()))
result=bubble_sort(arr)
print("sorted result",result)

            
    ####descending bubble sort
def bubble_sort(arr):
    n = len(arr)

    for passes in range(n):
        for j in range(n - 1 - passes):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = list(map(int, input("Enter the numbers: ").split()))

result = bubble_sort(arr)

print("Sorted result:", result)