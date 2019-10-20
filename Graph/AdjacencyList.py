"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: AdjacencyList.py
@time: 2019/10/20 19:12
"""
class AdjList:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
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
        visited = [False for i in range(self.V)]
        pre_order = [] # 前序遍历结果
        post_order = [] # 后序遍历结果

        def dfs(v):
            # 标记v顶点已经遍历过了
            visited[v] = True
            # 添加
            pre_order.append(v)
            for w in self.adj[v]:
                if visited[w] == False:
                    dfs(w)
            post_order.append(v)
        dfs(0)
        return pre_order,post_order

if __name__ == '__main__':
    adjm = AdjList("../g.txt")
    adjm.get_graph_information()
    print(adjm.hasEdge(0,4))
    print(adjm.degree(1))
    print(adjm.graphDFS())
