"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: BFS.py
@time: 2019/10/24 15:51
"""
import queue
class GraphBFS:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__cccount = 0 # 联通分量
        self.__order = [] # 广度优先遍历
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
        self.graphBFS()

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

    def hasEdge(self, v, w):
        """
        判断两个顶点是否存在
        :param v: 第一个顶点
        :param w: 第二个顶点
        :return: true or false
        """
        self.validateVertex(v)
        self.validateVertex(w)
        return w in self.adj[v]

    def degree(self, v):
        """
        求某个顶点的度
        :param v:
        :return:
        """
        self.validateVertex(v)
        return len(self.adj[v])


    def graphBFS(self):
        visited = [False for i in range(self.V)]
        order = []

        def bfs(v):
            # 使用队列来存放经过结点
            que = queue.Queue(self.V)
            # 经过顶点v时，将v放进队列中
            que.put(v)
            visited[v] = True
            # 队列为空时，即在某个联通分量已经遍历完毕
            while que.empty() == False:
                # 取出v 并做标记将v放入order 后面开始对v的邻点遍历
                v = que.get()
                order.append(v)

                for w in self.adj[v]:
                    if visited[w] == False:
                        que.put(w)
                        visited[w] = True

        for i in range(self.V):
            if visited[i] == False:
                bfs(i)
        self.__order = order

    def get_cccount(self):
        """
        获取该图的联通分量
        :return:
        """
        return self.__cccount

    def get_BFSorder(self):
        """
        获取该图的广度优先搜素
        :return:
        """
        print("广度优先搜索：{}".format(self.__order))

if __name__ == '__main__':
    bfs = GraphBFS("../g.txt")
    bfs.get_graph_information()
    bfs.get_BFSorder()
