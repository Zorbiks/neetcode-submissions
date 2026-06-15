class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, a in enumerate(nums):
            mul = 1
            for j, b in enumerate(nums):
                if i != j:
                    mul*=b
            result.append(mul)
        return result


