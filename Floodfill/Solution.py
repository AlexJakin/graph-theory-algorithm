"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: Solution.py
@time: 2019/10/27 13:38
"""

class Solution(object):

    def __init__(self):
        self.__R = 0 # row
        self.__C = 0 # colum
        self.dirs = [
            [-1, 0], [0, 1], [1, 0], [0, -1]
        ]
        self.visited = []
        self.grid = []
        self.G = []

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

        self.G = self.constructGraph()
        # 对每一个陆地进行遍历
        res = 0
        self.visited = [False for i in range(len(self.G))]
        for v in range(len(self.G)):
            x = int(v / self.__C)
            y = v % self.__C
            if self.grid[x][y] == 1 and self.visited[v] == False:
                res = max(res, self.dfs(v))
        return res

    def dfs(self, v):
        self.visited[v] = True
        res = 1
        for w in self.G[v]:
            if self.visited[w] == False:
                res += self.dfs(w)
        return res


    def constructGraph(self):
        g = [[] for i in range(self.__R * self.__C)]

        # 二维转一维
        for v in range(len(g)):
            x = int(v / self.__C)
            y = v % self.__C
            # 一维表中某个位置计算出的(x, y) 代表 二维表中的坐标
            if self.grid[x][y] == 1:
                # 对(x, y)四个方向都进行观察，看看是否有陆地
                # 如果有，在邻接表中相应位置 增加一条边
                for d in self.dirs:
                    next_x = x + d[0]
                    next_y = y + d[1]
                    if self.inArea(next_x, next_y) and self.grid[next_x][next_y] :
                        next = next_x * self.__C + next_y
                        g[v].append(next)
                        g[next].append(v)
        return g

    def inArea(self, x, y):
        return x >= 0 and x < self.__R and y >= 0 and y < self.__C



if __name__ == '__main__':
    obj = Solution()
    print(obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))