from math import *


def count(nums): # O(log10(N))
    count = 0
    while nums > 0:
        count = count + 1
        nums = nums // 10
    return count


def count_using_log(nums): # O(1)
    return int(log10(nums) + 1)


nums = int(input("Enter your number: "))
# c = count(nums)
c = count_using_log(nums)
l = log10(nums)
print(l)
print(f"this is your count of numbers {c}")