## Using recursion funnction chack the string is palindrome or not

def palindrome(s, l, r):
    if l >= r:
        print("String is palindrome")
        return
    if s[l] != s[r]:
        print("String is not a palindrome")
        return False
    palindrome(s, l+1, r-1)

s = "hah"
palindrome(s, 0, len(s)-1)
