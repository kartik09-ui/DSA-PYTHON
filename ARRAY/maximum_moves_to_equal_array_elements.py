class Solution:
    def minMoves(self, nums) -> int:
        n = len(nums)
        c = 0
        max = 0
        for i in range(n):
            if max < nums[i]:
                max = nums[i]
        for i in range(n):
            if nums[i] != max:
                diff = max - nums[i]
                c = c + diff
        return c
        