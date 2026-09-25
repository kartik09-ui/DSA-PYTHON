

def second_largest_element(nums): # TC -> O(N+N)
                                 # SC -> O(1)
    n = len(nums)
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(0, n):
        if largest < nums[i]:
            largest = nums[i]

    for i in range(0, n):
        if second_largest < nums[i] and nums[i] != largest:
            second_largest = nums[i]
    print(second_largest)


### OPTIMAL SOLUTION
def find_second_largest_element(nums):
    n = len(nums)
    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(0, n):
        if largest < nums[i]:
            second_largest = largest
            largest = nums[i]
        elif second_largest < nums[i] and nums[i] != largest:
            second_largest = nums[i]
    print(second_largest)
nums = [55, 32, 97, -55, 45, 32, 88, 21]
S = find_second_largest_element(nums)