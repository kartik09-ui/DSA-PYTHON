nums = [0,1,-1,2,4,0,-1,0,-2]

#  brute force
def find_3_sum_1(nums):
    my_set = set()
    n = len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    my_set.add(tuple(temp))
    return [list(ans) for ans in my_set]



# better
def find_3_sum_2(nums):
    res = set()
    n = len(nums)
    for i in range(0,n):
        my_set = set()
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in my_set:
                temp = [nums[i],nums[j],third]
                temp.sort()
                res.add(tuple(temp))
            my_set.add(nums[j])
    return [list(ans) for ans in res]


# optimal

def find_3_sum_3(nums):
    n = len(nums)
    i = 0
    res = []
    nums.sort()
    while i < n:
        if i != 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n-1
        while j <= k:
            total_sum = nums[i]+nums[j]+nums[k]
            if total_sum < 0:
                j+=1
            elif total_sum > 0:
                k-=1
            else:
                temp = [nums[i],nums[j],nums[k]]
                res.append(temp)   
                # skipping the duplicates if occured
                while j<k and nums[j] == nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
        return res




# f = find_3_sum(nums)
# print(f) 