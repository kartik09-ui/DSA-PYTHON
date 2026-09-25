def find_maximum_subarray_sum(nums):
    n = len(nums)
    total = 0
    max_i = float('-inf')
    for i in range(0,n):
        if total < 0:
            total = 0
        total+=nums[i]
        if total > max_i:
            max_i = total
        