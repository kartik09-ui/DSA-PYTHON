def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):  # TC -> O(N(N+1)/2)  -> O(N**2)
        min_index = i      # SC -> O(1)
        for j in range(i + 1, n):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

nums = [2,6,8,3,1,1,4]
s = selection_sort(nums)
print(s)