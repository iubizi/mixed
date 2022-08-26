class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for num in nums:
            if num == 1:
                sum += 1
                ans = max(ans, sum)
            else:
                sum = 0
        return ans
