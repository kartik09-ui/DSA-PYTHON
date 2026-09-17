### In recursion we have its 2 types head recursion and tail rcursion
### In Head recursion we first do the job and then call the recursive function
### In Tail recursion ew call recursive function then do the job we also know it as backtracking

# HEAD RECURSION 
# print 1 to n
def head(i,n):
    if i>n:
        return 
    print(i)
    head(i+1, n)

# TAIL RECURSION
# print n to 1
def tail(i, n):
    if i>n:
        return
    tail(i+1, n)
    print(i)

# Print 1 to N using TAIL
def one_to_N(n):
    if n == 0:
        return 
    one_to_N(n-1)
    print(n)


head(1, 5)
print("\n")
tail(1, 5)
print("\n")
one_to_N(5)