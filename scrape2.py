from collections import defaultdict
hash1 = defaultdict (dict,{1:"a", 2:'b'})
list1 = [9,8,7]
# print (hash1[1])
# print (list1[0])


for neighbor in hash1[0]: # output is nothing
    print('neighbor =========',neighbor)
for neighbor in hash1[1]: # neighbor ========= a
    print('neighbor =========',neighbor)
