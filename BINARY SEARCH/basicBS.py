
#  Iterative solution
def binary_search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

#  Recuursive solution
def binary_search_recursive(nums,low,high,target):
    if low > high:
        return -1
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search_recursive(nums,low,mid-1,target)
    else:
        return binary_search_recursive(nums,mid+1,high,target)
    

nums = [1,2,3,4,5,6,7,8]
BS = binary_search_recursive(nums,low=0,high=len(nums),target=7)
print(BS)

