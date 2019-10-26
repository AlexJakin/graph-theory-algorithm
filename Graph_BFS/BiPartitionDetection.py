"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: BiPartitionDetection.py
@time: 2019/10/26 16:11
"""
import queue
class BiPartitionDetection:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__initGraph(filename)
        self.__isBiPartitie = True

        # 检测二部图
        self.visited = [False for i in range(self.V)]
        self.colors = [-1 for i in range(self.V)]
        for v in range(self.V):
            if self.visited[v] == False:
                if self.bfs(v) == False:
                    self.__isBiPartitie = False
                    break


    def __initGraph(self, filename):
       with open(filename) as f:
            line_num = 0  # 第一行是顶点数和边数
            for line in f:
                if line_num == 0:
                    v, e = line.strip().split()
                    self.V = int(v)
                    self.E = int(e)
                    self.adj = [[] for i in range(self.V)] # 创建二维数组即邻接表
                else:
                    # 读取边 写入邻接表
                    v1, v2 = line.strip().split()
                    # 转化为整数
                    v1 = int(v1)
                    v2 = int(v2)
                    self.adj[v1].append(v2)
                    self.adj[v2].append(v1)
                line_num += 1

    def bfs(self, s):
        que = queue.Queue(self.V)
        # 往队列中添加顶点s
        que.put(s)
        self.visited[s] = True
        self.colors[s] = 0

        while que.empty() == False:
            v = que.get()

            for w in self.adj[v]:
                if self.visited[w] == False:
                    que.put(w)
                    self.visited[w] = True
                    self.colors[w] = 1 - self.colors[v]
                elif self.colors[w] == self.colors[v]:
                    return False
        return True

    def isBiPartite(self):
        return self.__isBiPartitie

if __name__ == '__main__':
    print("=====first graph======")
    g = BiPartitionDetection("g.txt")
    print(g.isBiPartite())
    print("=====second graph======")
    g = BiPartitionDetection("g2.txt")
    print(g.isBiPartite())
    print("=====third graph======")
    g = BiPartitionDetection("g3.txt")
    print(g.isBiPartite())