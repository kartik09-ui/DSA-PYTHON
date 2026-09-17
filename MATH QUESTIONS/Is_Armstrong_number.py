
def find_armstrong(nums): ## TC -> O(log10(N))
    l = len(str(nums))
    total = 0
    while nums > 0:
        digit = nums % 10
        total = total + digit ** l
        nums = nums // 10
    print(f"{total}")
    

nums = int(input("Enter  Your Number: "))
A = find_armstrong(nums)
