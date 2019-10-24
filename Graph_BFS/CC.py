"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: CC.py
@time: 2019/10/24 20:42
"""
import queue
# 联通分量
class CC:
    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__cccount = 0 # 联通分量
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

        self.__visited = [-1 for i in range(self.V)]
        # 对每个顶点进行遍历
        for i in range(self.V):
            if self.__visited[i] == -1:
                self.bfs(i, self.__cccount)
                self.__cccount += 1

    # 非递归
    def bfs(self, s, ccid):
        que = queue.Queue(self.V)
        # 将经过的点放入队列中
        que.put(s)
        self.__visited[s] = ccid
        # 队列为空的时候说明此时已经遍历结束
        while que.empty() == False:
            # 取出s的相邻顶点v，并对v的相邻顶点w遍历，将遍历过的顶点在visited数组中做标记
            v = que.get()
            for w in self.adj[v]:
                if self.__visited[w] == -1:
                    que.put(w)
                    self.__visited[w] = ccid

    def get_ccount(self):
        print("联通分量大小为：{}".format(self.__cccount))

    def get_components(self):
        res = [[] for i in range(self.__cccount)]

        for i in range(self.V):
            res[self.__visited[i]].append(i)
        print("各联通分量为：{}".format(res))

if __name__ == '__main__':
    cc = CC("../g_ssp.txt")
    cc.get_ccount()
    cc.get_components()