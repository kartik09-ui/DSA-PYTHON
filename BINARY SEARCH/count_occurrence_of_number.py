def find_lower_bound(nums,target):
    lb = -1
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb

def find_upper_bound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub

nums = [1,2,3,3,3,3,3,4,5,6,6,6]
lb = find_lower_bound(nums,3)
ub = find_upper_bound(nums,3)
print(ub-lb)