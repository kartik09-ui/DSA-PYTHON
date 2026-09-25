nums = [55, 32, -97, 99, 3, 67]

n = len(nums)
# largest = nums[0]
largest = float("-inf")
for i in range(0, n):
    # largest = max(largest, nums[i])
    if largest < nums[i]:
        largest = nums[i]

print(largest)