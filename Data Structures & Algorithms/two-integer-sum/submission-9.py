class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indices = []
        for i, n in enumerate(nums):
            difference = target - n
            if difference in seen:
                indices.append(i)
                indices.append(seen[difference])
                indices.sort()
            seen[n] = i
        return indices