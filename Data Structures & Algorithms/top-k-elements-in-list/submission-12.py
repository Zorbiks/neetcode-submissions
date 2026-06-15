class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        freq_list = list(freq.items())
        freq_list_sorted = sorted(freq_list, key=lambda kv: kv[1], reverse=True)
        result = []
        for i in freq_list_sorted[:k]:
            result.append(i[0])
        return result
