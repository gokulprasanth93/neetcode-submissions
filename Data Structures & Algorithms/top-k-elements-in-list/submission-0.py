class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = seen[num]+1
            else:
                seen[num] = 1 

        sorted_dict = sorted(seen.items(), key = lambda x:x[1], reverse= True) 

        values = [key for key, value in sorted_dict[:k]]   
        return values   