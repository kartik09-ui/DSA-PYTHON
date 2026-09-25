def find_two_sum(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i


nums = [2,3,5,8,6,9]
target = 13
t = find_two_sum(nums,target)
print(t)