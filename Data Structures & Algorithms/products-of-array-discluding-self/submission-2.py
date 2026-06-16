class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        i = 1
        while i < len(nums):
            mul = nums[i-1] * prefix[i-1]
            prefix.append(mul)
            i += 1
        
        # The indexing on this one is kinda confusing
        # I just copied the loop from before
        # And Bruteforced the indexing kinda
        i = len(nums) - 2
        while i > -1:
            mul = nums[i+1] * suffix[len(nums) - i - 2]
            suffix.append(mul)
            i -= 1
        
        final = []
        i = 0
        while i < len(suffix):
            final.append(prefix[i] * suffix[len(suffix) - 1 - i])
            i+=1
        
        return final