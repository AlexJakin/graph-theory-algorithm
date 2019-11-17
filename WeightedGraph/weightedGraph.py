"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: weightedGraph.py
@time: 2019/10/20 19:12
"""
class weightedGraph:

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
                    self.adj = [{} for i in range(self.V)] # 创建二维数组 且 以字典为单位即邻接表
                else:
                    # 读取边 写入邻接表
                    v1, v2, w = line.strip().split()
                    # 转化为整数
                    v1 = int(v1)
                    v2 = int(v2)
                    w = int(w)
                    self.adj[v1][v2] = w
                    self.adj[v2][v1] = w
                line_num += 1
        print(self.adj)
        print(self.adj[0])
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

    def getWeight(self, v, w):
        if self.hasEdge(v, w):
            return self.adj[v][w]

    def degree(self, v):
        """
        求某个顶点的度
        :param v:
        :return:
        """
        self.validateVertex(v)
        return len(self.adj[v])


    def graphDFS(self):
        visited = [False for i in range(self.V)]
        pre_order = [] # 前序遍历结果
        post_order = [] # 后序遍历结果
        cccount = 0 # 联通分量

        def dfs(v):
            # 标记v顶点已经遍历过了
            visited[v] = True
            # 添加
            pre_order.append(v)
            for w in self.adj[v]:
                if visited[w] == False:
                    dfs(w)
                    # 此刻对某个顶点的邻点已经遍历结束
            post_order.append(v)

        # 顾及到有多个联通分量，对每个顶点都做DFS
        for i in range(self.V):
            if visited[i] == False:
                dfs(i)
                cccount += 1
        self.__cccount = cccount
        return pre_order,post_order

    def get_cccount(self):
        """
        获取该图的联通分量
        :return:
        """
        return self.__cccount

if __name__ == '__main__':
    weighted_graph = weightedGraph("g.txt")
    print(weighted_graph.getWeight(0, 1))

