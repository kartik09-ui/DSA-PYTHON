def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):  # TC -> O(N**2)  SC -> O(1)
        key = nums[i]
        j = i
        while j <= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j = j-1
        nums[j+1] = key

