### Q. Revese an array from left to right where left and right are the int in the range of length of array
### let arr = [2,4,6,7,2,8,9,1,5] 
# len of arr   0 1 2 3 4 5 6 7 8
# left  = 2 and right = 7
# output arr = [1, 9, 8, 2, 7, 6]


def reverse_array(arr, l, r):
    if l >= r:
        print(arr)
        return 
    arr[l], arr[r] = arr[r], arr[l]
    reverse_array(arr, l+1, r-1)

arr = [2,4,6,7,2,8,9,1,5]
reverse_array(arr, 2, 7)