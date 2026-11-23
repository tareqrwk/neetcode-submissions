class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for number in nums:
            if number not in counts:
                counts[number] = 1
            counts[number] += 1
        sorted_keys = sorted(counts, key = lambda n: counts[n], reverse = True)
        return sorted_keys[:k]
