def bubble_sort(nums):
    n = len(nums)
    for i in range(0, n):  # TC -> O(N(N+1)/2)  -> O(N**2)
        for j in range(0, n-i-1):   # SC -> O(1)
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [2,4,6,1,3,8,5]
b = bubble_sort(nums)
print(nums)