def character_hash(s, q):
    hash_list = [0] * 25
    for ch in s:
        ascii_val = ord(ch)
        index = ascii_val - 97
        hash_list[index] += 1

    for ch in q:
        ascii_val = ord(ch)
        index = ascii_val - 97
        print(hash_list[index])

s = "kjfwiuhfkjh"

q = ['k','f','g','w']

d = character_hash(s, q)