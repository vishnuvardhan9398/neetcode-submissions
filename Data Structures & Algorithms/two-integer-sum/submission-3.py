class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     d = {}
     for i in range(len(nums)):
        num = nums[i]
        c = target - num
        if c in d:
            return [d[c],i]
        d[num] = i
     return []        