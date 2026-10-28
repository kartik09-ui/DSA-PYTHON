def containsDuplicate(self, nums: list[int]) -> bool:
    # nums.sort()
    # n = len(nums)
    # s = 0
    # f = 1
    # while f<n:
    #     if nums[s] == nums[f]:
    #         return True
    #     s+=1
    #     f+=1
    # return False

    n = len(nums)
    s = set()
    for i in range(n):
        if nums[i] in s:
            return True
        s.add(nums[i])
    return False