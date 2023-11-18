

'''   0
    /  |  \
   1   2   3
/   \  /
4     5
  '''
ad_max = [
   #0 1 2 3 4 5           # print ad-max[n]
   [0,1,1,1,0,0],#0    # 0 line 2 times  # 5 line 5 times
   [1,0,0,0,1,1],#1    # 1 line 5 times  # 3 line 6 times
   [1,0,0,0,0,1],#2    # 4 line 6 time   # 0 line 2 times
   [1,0,0,0,0,0],#3    # 2 line 1  time
   [0,1,0,0,0,0],#4    # 5 line 3  time
   [0,1,1,0,0,0] #5    # 2 line 6  time
]
visited= [0,0,0,0,0,0] #indicates if a node has been visited or not
# n = means a node
#what are the numbers in the matrix?
#what are the numbers in visited?
#where is the relation?
# why is relation different when we put it in teh for loop and outside the for loop?
#where is the visited?
#where is the n?
# what is num? why do we have it?
def dfs (n):
    if visited[n] != 0:
        return
    else:
        visited[n] = 1 # this means if node is not visited then mark it as visited
        num = 0
        for relation in ad_max[n]:
            # print(relation)
            print (ad_max[n])
            if relation != 0:
                dfs(num) # recursively calls the dfs function for each adjacent node that is connected.
            num = num + 1 # this will be used to iterate over the adjacent nodes of the current node n
            # print (relation)
            # print (num)
        # print (n)
        # print (visited)
        # print (relation)
        # print (num)


# src_node = int(input('Enter the source node: '))
# dfs(src_node)
print (dfs(0))
