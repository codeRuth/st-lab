import sys

arr = [int(x) for x in sys.argv[1:]]

def partition(arr, first, last):
    if first < last:
        pivot = first
        i = first
        j = last
        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i+=1
            while arr[j] > arr[pivot]:
                j-=1
            if i < j:
                # temp = arr[i]
                # arr[i] = arr[j]
                # arr[j] = temp
                arr[i], arr[j] = arr[j], arr[i]

        # temp = arr[pivot]
        # arr[pivot] = arr[j]
        # arr[j] = temp
        arr[pivot], arr[j] = arr[j], arr[pivot]

    return j
    

def quicksort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quicksort(arr, low, part - 1)
        quicksort(arr, part + 1, high)

quicksort(arr, 0, len(arr) - 1)
print(arr)