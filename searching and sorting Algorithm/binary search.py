def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    for i in range(len(arr)):
        if low > high:
            break

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = list(map(int, input("Enter the number: ").split()))

target = int(input("Enter target: "))

result = binary_search(arr, target)
print(result)