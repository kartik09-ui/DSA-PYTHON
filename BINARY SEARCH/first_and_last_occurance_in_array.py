def lower_bound(nums,target):
    lb = -1
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb

def upper_bound(nums,target):
    ub = -1
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub


nums = [1,2,3,3,3,3,3,4,5,6,7,8,9,10]
lb = lower_bound(nums,3)
# if lb == -1:
#     return [-1,-1]
ub = upper_bound(nums,3)
print([lb,ub-1])