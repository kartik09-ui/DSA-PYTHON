## A Number is palindrome if reverse of the no. is same as the original number
## like 1221 is palindrome because its reverse is also 1221

def Find_reverse(nums):
    reverse_num = 0
    while nums >= 0:
        digit = nums % 10
        reverse_num = reverse_num * 10
        reverse_num = reverse_num + digit 
        nums = nums // 10
    return reverse_num


def Is_palindrome(nums, reverse_num):
    if nums == reverse_num:
        print('Yes given number is a palindrome')
    else:
        print("Given numbers is not a palindrome")




nums = int(input("Enter your number"))
R = Find_reverse(nums)
P = Is_palindrome(nums, R)