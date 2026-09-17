
def find_n_in_m(n, m):
    hash_list = [0] * 11
    for num in n:
        hash_list[num] = hash_list[num] + 1

    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(hash_list[num])


## using Hashing
def find_n_in_m2(n, m): # Wrong code 
    hash_map = {}
    l = len(n)
    for i in n:
        hash_map[n[i]] = hash_map.get(n[i], 0) + 1

    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(hash_map)


n = [3,5,3,3,5,7,2,1,5,3,7,9,4,2,5,8]  # 1<=n<=10

m = [4,6,2,23,65,7,5]
f = find_n_in_m(n, m)