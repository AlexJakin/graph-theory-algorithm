"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: EulerLoop.py
@time: 2019/10/20 19:12
"""
class EulerLoop:

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

        # dfs遍历
        self.graphDFS()

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


    def hasEulerLoop(self):

        # 联通分量判断
        if self.get_cccount() > 1:
            print("该图不存在欧拉回路（Euler Loop）")
            return False

        # 度数判断
        for v in range(self.V):
            if self.degree(v) % 2 == 1:
                print("该图不存在欧拉回路（Euler Loop）")
                return False

        print("该图存在欧拉回路（Euler Loop）")
        return True

if __name__ == '__main__':
    ELD = EulerLoopDetection("g.txt")
    ELD.get_graph_information()
    ELD.hasEulerLoop()

    ELD2 = EulerLoopDetection("g2.txt")
    ELD2.get_graph_information()
    ELD2.hasEulerLoop()
