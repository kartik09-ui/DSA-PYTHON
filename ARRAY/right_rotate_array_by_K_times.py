
nums = [3, 4, 5, 6, 7, 8, 9, 1, 2]

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def right_rotate_by_k_places(nums, k):
    n = len(nums)
    k = k % n

    # Step 1: Reverse entire array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(nums, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(nums, k, n - 1)

    return nums


k = 2
r = right_rotate_by_k_places(nums, k)
print(r)

