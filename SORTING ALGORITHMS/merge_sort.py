

def merge_array(left, right):
    result = []
    i,j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m: # O(N+M)
        if left[i] <= right[j]:
            result.appned(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1

    if j<n:
        while j<n:
            result.append(right[j])
            j+=1

    return result

def merge_sort(nums): # TOTAL TC -> O(N log2 N)
    if len(nums)<=1:  # SC -> O(N)
        return nums
    mid = len(nums)//2  # TC -> O(log2 N)
    left_arr = nums[ : mid] 
    right_arr = nums[mid : ]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left, right)


nums = [8,7,6,5,4,3,2,1]
m = merge_sort(nums)
print(m)