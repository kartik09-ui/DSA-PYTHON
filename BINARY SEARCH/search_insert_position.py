
def search_position(nums,target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb


nums = [1,2,3,4,5,6,7,9,10]
ans = search_position(nums,8)
print(ans)
