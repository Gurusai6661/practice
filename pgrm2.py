arr = [0, 3, 0, 2, 4]
# zeros together
def zerostogether(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
zerostogether(arr)
print("After pushing zeros to end:", arr)
