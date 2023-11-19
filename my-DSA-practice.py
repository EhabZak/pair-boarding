ad_max = [

   #0 1 2 3 4 5
   [0,1,1,1,0,0],#0    # 0 line 2 times  # 5 line 5 times # this line represents the node 0
   [1,0,0,0,1,1],#1    # 1 line 5 times  # 3 line 6 times
   [1,0,0,0,0,1],#2    # 4 line 6 time   # 0 line 2 times
   [1,0,0,0,0,0],#3    # 2 line 1  time
   [0,1,0,0,0,0],#4    # 5 line 3  time
   [0,1,1,0,0,0]
]

visited = [0,0,0,0,0,0]

def dfs (n) :
    if visited [n] != 0:
        return
    else:
        visited[n] = 1
        num = 1
        for relation in ad_max[n]:
            if relation != 0:
                dfs(n)
            num = num + 1
        print(n)
#you can also do it without recursion
