

'''   0
    /  |  \
   1   2   3
/   \  /
4     5
  '''
ad_max = [
  # these columns represent the relationship
   #0 1 2 3 4 5          # print ad-max[n]
   [0,1,1,1,0,0],#0    # 0 line 2 times  # 5 line 5 times # this line represents the node 0
   [1,0,0,0,1,1],#1    # 1 line 5 times  # 3 line 6 times
   [1,0,0,0,0,1],#2    # 4 line 6 time   # 0 line 2 times
   [1,0,0,0,0,0],#3    # 2 line 1  time
   [0,1,0,0,0,0],#4    # 5 line 3  time
   [0,1,1,0,0,0] #5    # 2 line 6  time
]
visited= [0,0,0,0,0,0] #indicates if a node has been visited or not
# n = means a node
#what are the numbers in the matrix? relationships to the node
#what are the numbers in visited? tracking the status of the node if visited or not
#where is the relation? in the matrix columns the rows represent the nodes
# why is relation different when we put it in the for loop and outside the for loop?
#where is the visited?
#where is the n? n = node the rows are the nodes or the n
# what is num? why do we have it? it represent the index of the numbers (which represent the relationship) in the ad_max[n] so the arrays in the ad_max array
def dfs (n):
    if visited[n] != 0: #! this is the base case
        return
    else:
        visited[n] = 1 # this means if node is not visited then mark it as visited
        num = 0 #! num is initiated here it means start at index zero in the ad_max[n]
        for relation in ad_max[n]: # for the numbers in the array of node 0 = [0,1,1,1,0,0]

            if relation != 0:
                dfs(num) # recursively calls the dfs function for each adjacent node that is connected.
            num = num + 1 # this will be used to iterate over the adjacent nodes of the current node n

        print (n)



# src_node = int(input('Enter the source node: '))
# dfs(src_node)
print (dfs(0))

# you can also do it like in mode 6 for both dfs and bfs and then solve the problems
#don't forget that there are also sort methods
