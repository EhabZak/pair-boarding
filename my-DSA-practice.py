from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        bucket = [[] for _ in range(n+1)]
        print(bucket)


        for char,freq in c.items():
            print(char)
            bucket[freq].append(char)
            print(bucket)

        res = ''
        for freq in range(n,0,-1):
            print('======',freq)
            for char in bucket[freq]:
                res += char*freq
        return res


s ="Abcddeeeee"
# s = "Aabb"
# s = "tree"
output = Solution().frequencySort(s)
print(output)
