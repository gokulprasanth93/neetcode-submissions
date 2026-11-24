class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for  ind, num in enumerate(nums):
            compliment = target - num
            if compliment not in seen:
                seen[num] = ind
            elif compliment in seen:
                return [seen[compliment], ind]

        