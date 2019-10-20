"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: AdjacencyMatrix.py
@time: 2019/10/20 18:31
"""
# 邻接矩阵
class AdjMatrix:

    def __init__(self, filename):
        self.V = 0 # 顶点数
        self.E = 0 # 边数
        self.adj = None
        with open(filename) as f:
            line_num = 0 # 第一行是顶点数和边数
            for line in f:
                if line_num == 0:
                    v, e = line.strip().split()
                    self.V = int(v)
                    self.E = int(e)
                    # self.adj = [[0] * self.V] * self.V # 该创建方式不正确 修改任何一个元素都会改变整个列表
                    self.adj = [([0] * self.V) for i in range(self.V)] # 创建二维数组即邻接矩阵
                else:
                    # 读取边 写入邻接矩阵
                    v1, v2 = line.strip().split()
                    # 转化为整数
                    v1 = int(v1)
                    v2 = int(v2)
                    self.adj[v1][v2] = 1
                    self.adj[v2][v1] = 1
                line_num += 1

    def get_graph_information(self):
        """
        打印图的邻接矩阵
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        print(adjm.adj)

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
        return self.adj[v][w]==1

    def degree(self, v):
        """
        求某个顶点的度
        :param v:
        :return:
        """
        self.validateVertex(v)
        return sum(self.adj[v])

    def AdjMatrixDFS(self):
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
        for i in range(self.V):
            if visited[i] == False:
                dfs(i)
        return pre_order,post_order

if __name__ == '__main__':
    adjm = AdjMatrix("../g.txt")
    adjm.get_graph_information()
    print(adjm.hasEdge(6, 6))
    print(adjm.degree(1))
    print(adjm.AdjMatrixDFS())