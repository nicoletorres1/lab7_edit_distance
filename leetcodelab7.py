'''
Author: Nicole Torres
CS2302: lab 7 extra credit
Date: 12/05/18
'''


# 120 Triangle leetcode
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


# 64. Minimum path sum
class Solution2:
    def minPathSum(self, matrix):
        m = len(matrix); n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + matrix[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        return dp[m-1][n-1]


def main():
    a = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

    solu1 = Solution()

    print(solu1.minimumTotal(a))

    b = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
        ]

    solu2 = Solution2()

    print(solu2.minPathSum(b))


main()
