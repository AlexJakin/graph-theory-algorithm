"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: CycleDetection.py
@time: 2019/10/22 15:48
"""
# 环检测（邻接矩阵）
class CycleDetection:

    def __init__(self, filename):
        self.V = 0 # 顶点数
        self.E = 0 # 边数
        self.adj = None
        self.__hasCycle = None
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

        # 初始化图时，进行深度优先搜索
        self.graphDFS()

    def get_graph_information(self):
        """
        打印图的邻接矩阵
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        print(self.adj)

    def validateVertex(self, v):
        """
        验证顶点取值
        :param v:
        :return:
        """
        if v<0 or v>=self.V:
            raise ValueError("v值超出范围")


    def graphDFS(self):
        visited = [False for i in range(self.V)]

        def dfs(v, parent):
            # 标记v顶点已经遍历过了
            visited[v] = True
            for w in self.adj[v]:
                if visited[w] == False:
                    dfs(w, v)
                else:
                    if w != parent:
                        return True
            return False

        for i in range(self.V):
            if visited[i] == False:
                if dfs(i, i):
                    self.__hasCycle = True
                    break

    def hasCycle(self):
        if self.__hasCycle:
            print("该图存在环")
        else:
            print("该图没有环")

# 环检测（邻接表）
class CycleDetection_v2:

    def __init__(self, filename):
        self.V = 0 # 顶点数
        self.E = 0 # 边数
        self.adj = None
        self.__hasCycle = None
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

        # 初始化图时，进行深度优先搜索
        self.graphDFS()

    def get_graph_information(self):
        """
        打印图的邻接矩阵
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


    def graphDFS(self):
        visited = [False for i in range(self.V)]

        def dfs(v, parent):
            # 标记v顶点已经遍历过了
            visited[v] = True
            for w in self.adj[v]:
                if visited[w] == False:
                    # if dfs(w, v):
                    #     return True
                    dfs(w, v)
                    print(v, w, parent)
                else:
                    if w != parent:
                        print(v, w, parent)
                        return True
            return False

        # 顾及到有多个联通分量，对每个顶点都做DFS
        for i in range(self.V):
            if visited[i] == False:
                if dfs(i, i):
                    self.__hasCycle = True
                    break

    def hasCycle(self):
        if self.__hasCycle:
            print("该图存在环")
        else:
            print("该图没有环")

if __name__ == '__main__':
    CD = CycleDetection("../g_cycle.txt")
    CD.get_graph_information()
    CD.hasCycle()
    print("=======第二种========")
    CD2 = CycleDetection_v2("../g_cycle.txt")
    CD2.get_graph_information()
    CD2.hasCycle()