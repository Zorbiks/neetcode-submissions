class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for index, num in enumerate(nums):
            a = target - num
            if a in nums:
                if a in indexes:
                    return [indexes[a], index]
                indexes[num] = index
        

