from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [ [1] * i for i in range(1, numRows + 1) ]

        for i in range(numRows):
            for j in range(i): # 最后一列已经被排除了，循环不到那里
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp


leetcode = Solution()
print(leetcode.generate(10))
