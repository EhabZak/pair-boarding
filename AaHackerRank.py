
#! Evaluate Reverse polish Notation

'''
put the question here

'''

# Complete the 'pol_notation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY tokens as parameter.
#

# def pol_notation(tokens):
#     opp = {
#         '+': lambda a,b: a+b,
#         '-': lambda a,b: a-b,
#         '/': lambda a,b: int(a/b),
#         '*': lambda a,b: a*b
#     }

#     stack = list()
#     for t in tokens:
#         if t not in opp:
#             stack.append(int(t))
#         else:
#             num = stack.pop()
#             num2= stack.pop()
#             stack.append(opp[t](num2,num))
#     return stack[0]


# tokens = ['2','1','+','3','*']
# print (pol_notation(tokens))

#!

'''
REST API top rated food outlets

'''

#
# Complete the 'getTopRatedFoodOutlets' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
#
# The function is expected to return an array of strings.
# The function accepts only city argument (String).
#

def getTopRatedFoodOutlets(city):
    # Write your code here
if __name__ == '__main__':
