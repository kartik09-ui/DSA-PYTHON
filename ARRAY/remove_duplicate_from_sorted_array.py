### In this qeustion there is a given array which is 
### sorted and holding duplicates we  have to find the 
### duplicates and change it to some other values and
### the remaining array is should be sorted 
### and return the total no. of uniqeu elements
### for ex - nums = [0,0,1,1,2,2,3,4,5,5] the output array is [0,1,2,3,4,5,_,_,_,_] and the no. of unique elements is 5


# Bruet Force solution
def remove_duplicates(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0, n):
        freq_map[nums[i]] = 0
    j = 0
    for k in freq_map:
        nums[j] = k
        j+=1
    return j

# Optimal Sulution
def remove_duplicates1(nums):

    n = len(nums)
    i=0
    j=i+1
    while j<n:
        if nums[i] != nums[j]:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
        j+=1
    return i+1


nums = [1,1,2,3,3,4,5,5,6,7,8,8]
r = remove_duplicates1(nums)
print(r)