"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: Solution2.py
@time: 2019/10/27 15:08
"""
class Solution2(object):

    def __init__(self):
        self.__R = 0 # row
        self.__C = 0 # colum
        self.dirs = [
            [-1, 0], [0, 1], [1, 0], [0, -1]
        ]
        self.visited = []
        self.grid = []

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None: return 0
        self.__R = len(grid)
        if self.__R == 0: return 0
        self.__C = len(grid[0])
        if self.__C == 0: return 0
        self.grid = grid

        # 对每一个陆地进行遍历
        res = 0
        self.visited = [[False for i in range(self.__C)] for i in range(self.__R)]
        for i in range(self.__R):
            for j in range(self.__C):
                if self.grid[i][j] == 1 and self.visited[i][j] == False:
                    res = max(res, self.dfs(i, j))
        return res

    def dfs(self, x, y):
        self.visited[x][y] = True
        res = 1
        for d in self.dirs:
            next_x = x + d[0]
            next_y = y + d[1]
            if self.inArea(next_x, next_y) and \
                    self.visited[next_x][next_y] == False and \
                    self.grid[next_x][next_y] == 1:
                res += self.dfs(next_x, next_y)
        return res


    def inArea(self, x, y):
        return x >= 0 and x < self.__R and y >= 0 and y < self.__C



if __name__ == '__main__':
    obj = Solution2()
    print(obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
