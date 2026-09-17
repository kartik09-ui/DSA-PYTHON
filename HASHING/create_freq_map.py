## This is the basic method to create a frequency map

# Method --> 1
def  FreqMap(nums):
    freq_map = {}
    for i in range(0, len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] = freq_map[nums[i]] + 1
        else:
            freq_map[nums[i]] = 1 

    return freq_map

def FreqMap2(nums):
    hash_map = {}
    for i in range(0,len(nums)):
        hash_map[nums[i]] = hash_map[nums[i]].get(nums[i],0) + 1
    return hash_map

nums = [1,3,1,43,5,3,2,3,2]
F = FreqMap(nums)
print(F)

