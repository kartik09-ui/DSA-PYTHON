#### in this question there is given a array of integers threr is one missing value we want to find that value 
# for example nums = [1,2,3,5,6,7,8,9] 
# to find missing value we calculate the sum of 1 to n using n(n+1)/2 
# and find the sum of elements substract both and the ans is our output


nums = [1,2,3,5,6,7,8,9]
n = len(nums) + 1
sum = 0
sum_n = n * (n + 1)//2
for i in range(n-1):
    sum = sum + nums[i]
ans = sum_n - sum
print(ans)