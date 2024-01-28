from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        count = Counter(s)


        bucket = [[] for _ in range(n+1)]

        for char, freq in count.items():
            bucket[freq].append(char)

        res = ''

        for index in range (n,0,-1):
            for char in bucket[index]:
                # print(char)
                res += char*index

        return res

# s ="Abcddeeeee"
# s = "Aabb"
s = "tree"
output = Solution().frequencySort(s)
print(output)
