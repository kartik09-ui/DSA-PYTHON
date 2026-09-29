def find_longest_consicutive_sequence(nums):
    n = len(nums)

    if len(nums) == 0:
        return 0

    nums.sort()

    last_smallest = float('-inf')
    count = 0
    longest = 0
    for i in range(0,n):
        num = nums[i]
        if num - 1 == last_smallest:
            count+=1
            last_smallest = num
        elif num!=last_smallest:
            count = 1
            last_smallest = num
        if count > longest:
            longest = count
    return longest