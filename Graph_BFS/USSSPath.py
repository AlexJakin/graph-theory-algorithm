"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: USSSPath.py
@time: 2019/10/26 16:41
"""
import queue
class USSSPath:

    def __init__(self, filename, s):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__initGraph(filename)

        # 计算路径和最短路径
        self.visited = [False for i in range(self.V)]
        self.__dis = [-1 for i in range(self.V)] # 记录每个结点离根节点的最小距离
        self.pre = [-1 for i in range(self.V)] # 每一个结点的上一个结点
        self.s = s
        self.bfs(s)

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

    def get_graph_information(self):
        """
        打印图的邻接表
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        for i, v in enumerate(self.adj):
            print("{} : {}".format(i, v))

    def validateVertex(self, v):
        """
        验证顶点取值
        :param v:
        :return:
        """
        if v<0 or v>=self.V:
            raise ValueError("v值超出范围")

    def bfs(self, s):
        que = queue.Queue(self.V)
        self.visited[s] = True
        que.put(s)
        self.pre[s] = s
        self.__dis[s] = 0
        while que.empty() == False:
            v = que.get()

            for w in self.adj[v]:
                if self.visited[w] == False:
                    que.put(w)
                    self.visited[w] = True
                    self.pre[w] = v
                    self.__dis[w] = self.__dis[v] + 1

    def isConnectedTo(self, t):
        self.validateVertex(t)
        return self.visited[t]

    def dis(self, t):
        self.validateVertex(t)
        print("{} -> {}的距离为：{}".format(self.s, t, self.__dis[t]))

    def path(self, t):
        res = []
        if self.isConnectedTo(t) == False:
            return res
        cur = t
        while cur != self.s:
            res.append(cur)
            cur = self.pre[cur]
        res.append(self.s)

        res.reverse()
        print("{} -> {}的路径为：{}".format(self.s, t, res))

if __name__ == '__main__':
    usssp = USSSPath("../g_ssp.txt", 0)
    usssp.get_graph_information()
    usssp.path(6)
    usssp.dis(6)