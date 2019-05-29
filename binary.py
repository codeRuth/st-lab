import sys

arr = [int(x) for x in sys.argv[1:-1]]
key = int(sys.argv[-1])

low = 0 
high = len(arr)

while low <= high:
    mid = int((low + high) / 2)
    if arr[mid] == key:
        print("Found at %d" % (mid + 1))
        exit()
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print("Not Found")