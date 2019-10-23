"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: CC.py
@time: 2019/10/20 19:12
"""
class CC:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__cccount = 0 # 联通分量
        self.__visited = None

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


    def graphDFS(self):
        visited = [-1 for i in range(self.V)]
        cccount = 0 # 联通分量

        def dfs(v, ccid):
            # 标记v顶点已经遍历过了
            visited[v] = ccid
            # 添加
            for w in self.adj[v]:
                if visited[w] == -1:
                    dfs(w, ccid)
                    # 此刻对某个顶点的邻点已经遍历结束

        # 顾及到有多个联通分量，对每个顶点都做DFS
        for i in range(self.V):
            if visited[i] == -1:
                dfs(i, cccount)
                cccount += 1
        self.__cccount = cccount
        self.__visited = visited


    def get_cccount(self):
        """
        获取该图的联通分量大小
        :return:
        """
        return self.__cccount

    def get_visited(self):
        """
        获取该图的联通分量列表
        :return:
        """
        return self.__visited

    def isConnected(self, v, w):
        """
        查看两个顶点是否在一个联通分量中
        :param v:
        :param w:
        :return:
        """
        self.validateVertex(v)
        self.validateVertex(w)
        return self.__visited[v] == self.__visited[w]

    def components(self):
        # 为每一个联通分量开辟空间
        res = [[] for i in range(self.__cccount)]
        for v in range(self.V):  # 遍历每一个顶点
            # 将相同联通分量的顶点放入同一个数组中, visited[0]=visited[1]=0, 则将0,1顶点放入索引为0的数组中
            res[self.__visited[v]].append(v)
        for i, row in enumerate(res):
            print("联通分量{}：{}".format(i, row))


if __name__ == '__main__':
    adjl = CC("../g_unconnected.txt")
    adjl.get_graph_information()
    print(adjl.graphDFS())
    print(adjl.get_cccount())
    print(adjl.get_visited())
    print(adjl.isConnected(0, 4))
    adjl.components()
