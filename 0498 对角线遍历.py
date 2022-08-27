from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        x, y = 0, 0
        ROW = len(mat)
        COL = len(mat[0])
        ans = []
        
        for _ in range(ROW * COL):
            
            ans.append(mat[x][y])
            # print(x, y)

            # 注意加法和百分号的优先级
            if (x+y) % 2 == 0: # 坐标之和等于偶数，向右上移动
                # 下面三个的顺序不能反，反了就错了
                if y == COL-1: x += 1 # 最后一列则向下运动
                elif x == 0: y += 1 # 第一行则向右运动
                else: x -= 1; y += 1 # 其余右上运动
            else: # 坐标之和等于奇数，向左下移动
                if x == ROW-1: y += 1 # 最后一行则向右运动
                elif y == 0: x += 1 # 第一列则向下运动
                else: x += 1; y -= 1 # 其余左下运动
                
        return ans


if __name__ == '__main__':

    mat = [ [1,2,3],[4,5,6],[7,8,9] ]
    
    leetcode = Solution()
    print(leetcode.findDiagonalOrder(mat))
