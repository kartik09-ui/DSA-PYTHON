
def right_rorate_array_once(nums):
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    return nums


nums = [3,4,5,6,7,8]
a = right_rorate_array_once(nums)
print(a)
## using slicing
# nums[:] = [nums[n-1]] + nums[0:n-1]
# print(nums)