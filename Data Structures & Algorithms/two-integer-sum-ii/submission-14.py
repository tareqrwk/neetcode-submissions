class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        indices = []
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
            if numbers[right] + numbers[left] > target:
                right -= 1
                continue
            if numbers[right] + numbers[left] == target:
                indices.append(left + 1)
                indices.append(right + 1)
                return indices