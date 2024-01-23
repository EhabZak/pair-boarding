
matrix = [11,22,33,44,55,66,77,22]
for r in range(len(matrix)):
    print (r ,matrix[r])
'''
0 11
1 22
2 33
3 44
4 55
5 66
6 77
7 22
    '''
for r in matrix:
    print (r)
'''
11
22
33
44
55
66
77
22
'''

matrix = [11,22,33,44,55,66,77,22]
for r in range(len(matrix)):
    def addNums(number):
        return number+ 100

added_numbers = map(addNums, matrix)

print(added_numbers) # <map object at 0x7f536c2ebfa0>
print(list(added_numbers)) # [111, 122, 133, 144, 155, 166, 177, 122]
print(tuple(added_numbers)) # ()
print(set(added_numbers)) # {}
print(dict(added_numbers)) # TypeError: cannot convert dictionary update sequence element #0 to a sequence

result_dict = dict(enumerate(added_numbers))
print (result_dict) # {0: 111, 1: 122, 2: 133, 3: 144, 4: 155, 5: 166, 6: 177, 7: 122}

added_numbers_list = list(map(addNums, matrix))
print("****" ,added_numbers_list) # [111, 122, 133, 144, 155, 166, 177, 122]
print("****" ,tuple(added_numbers_list)) # (111, 122, 133, 144, 155, 166, 177, 122)
print("****" ,set(added_numbers_list)) # {133, 166, 111, 144, 177, 122, 155}
