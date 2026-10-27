
def find_one_plus(nums):
    s = ""

    for num in nums:
        s += str(num)

    newN = int(s)
    newN += 1

    res = []
    while newN > 0:
        digit = newN % 10
        res.insert(0, digit)
        newN //= 10

    return res

nums = [1, 2, 9]
f = find_one_plus(nums)
print(f)

# my solution is perfect but another solution is -->
def find_one_plus1(nums):
    number = int("".join(map(str,nums)))+1
    return [int(digit) for digit in str(number)]
