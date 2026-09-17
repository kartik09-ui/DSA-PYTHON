def Reverse_number(nums):
    R_num = 0
    while nums > 0:
        digit = nums % 10
        R_num = R_num * 10
        R_num = R_num + digit
        nums = nums // 10
    return R_num

nums = int(input("Enter Your number: "))
r = Reverse_number(nums)
print(f"This ins the reverse of your given no. {r}")

