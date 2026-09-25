nums1 = [1,1,2,3,4,4,5]
nums2 = [2,2,5,6,7,7,8,9]

def merge_two_sorted_array(nums1,nums2):
    res = []
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 == 0 and n2 == 0:
        return
    i = 0
    j = 0
    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            if len(res) == 0 or res[-1] != nums1[i]:
                res.append(nums1[i])
            i+=1
        else:
            if len(res) == 0 or res[-1] != nums2[j]:
                res.append(nums2[j])
            j+=1

    while i<n1:
        if len(res) == 0 or res[-1] != nums1[i]:
            res.append(nums1[i])
        i+=1
    while j<n2:
        if len(res) == 0 or res[-1] != nums2[j]:
            res.append(nums2[j])
        j+=1
    return res

r = merge_two_sorted_array(nums1,nums2)
print(r)