def search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

nums = [11,12,13,1,2,3,4,5,6,7,8]
f = search(nums,9)
print(f)