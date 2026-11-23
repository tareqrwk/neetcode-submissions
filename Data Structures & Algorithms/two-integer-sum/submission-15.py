class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indices = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                indices.append(min(i, seen[difference]))
                indices.append(max(i, seen[difference]))
            seen[nums[i]] = i
        return indices