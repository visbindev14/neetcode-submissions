class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        if len(nums) == 1:
            return nums
        for i, num in enumerate(nums):
            dict[num] = dict.get(num, 0) + 1
        
        result = sorted(dict.keys(), key=lambda x: dict[x], reverse=True)
        return result[:k]