from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1. Count frequency of each number
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        # 2. Sort numbers based on their frequency
        sorted_nums = sorted(d, key=d.get, reverse=True)

        # 3. Take first k numbers
        return sorted_nums[:k]