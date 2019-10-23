"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: SingleSourcePath.py
@time: 2019/10/22 14:05
"""

class SingleSourcePath:

    def __init__(self, filename, s):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.s = s # 顶点s
        self.__pre = []
        self.__visited = [] # 该顶点所在的联通分量


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

    def graphDFS(self):
        visited = [False for i in range(self.V)]
        # pre[0]=-1 代表 顶点0在遍历时没顶点经过它，即他不在求单源路径的某个顶点的联通分量中
        pre = [-1 for i in range(self.V)]

        def dfs(v, parent):
            # 标记v顶点已经遍历过了
            visited[v] = True
            # 记录顶点v是从哪个顶点来的
            pre[v] = parent
            for w in self.adj[v]:
                if visited[w] == False:
                    dfs(w, v)
        dfs(self.s, self.s)
        self.__visited = visited
        self.__pre = pre

    def isConnectedTo(self, t):
        """
        判断到目标顶点t是否可达
        :param t: 目标
        :return:
        """
        self.validateVertex(t)
        return self.__visited[t]

    def path(self, t):
        """
        到目标顶点t的路径
        :param t:
        :return:
        """
        # 路径
        res = []
        # 若顶点t不在s的联通分量中
        if self.isConnectedTo(t) == False:
            print("{} -> {}的路径为：{}".format(self.s, t, res))
            return None
        cur = t
        while cur != self.s:
            res.append(cur)
            cur = self.__pre[cur]
        res.append(self.s)
        res.reverse()
        print("{} -> {}的路径为：{}".format(self.s, t, res))

# 只使用 pre一个数组
class SingleSourcePath_v2:

    def __init__(self, filename, s):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.s = s # 顶点s
        self.__pre = []


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

    def graphDFS(self):
        # pre[0]=-1 代表 顶点0在遍历时没顶点经过它，即他不在求单源路径的某个顶点的联通分量中
        pre = [-1 for i in range(self.V)]

        def dfs(v, parent):
            # 记录顶点v是从哪个顶点来的
            pre[v] = parent
            for w in self.adj[v]:
                if pre[w] == -1:
                    dfs(w, v)
        dfs(self.s, self.s)
        self.__pre = pre

    def isConnectedTo(self, t):
        """
        判断到目标顶点t是否可达
        :param t: 目标
        :return:
        """
        self.validateVertex(t)
        return self.__pre[t]

    def path(self, t):
        """
        到目标顶点t的路径
        :param t:
        :return:
        """
        # 路径
        res = []
        # 若顶点t不在s的联通分量中
        if self.isConnectedTo(t) == -1:
            print("{} -> {}的路径为：{}".format(self.s, t, res))
            return None
        cur = t
        while cur != self.s:
            res.append(cur)
            cur = self.__pre[cur]
        res.append(self.s)
        res.reverse()
        print("{} -> {}的路径为：{}".format(self.s, t, res))



if __name__ == '__main__':
    ssp = SingleSourcePath("../g_ssp.txt", 0)
    ssp.get_graph_information()
    ssp.path(6)
    ssp.path(5)
    print("===第二种方法===")
    ssp = SingleSourcePath_v2("../g_ssp.txt", 0)
    ssp.get_graph_information()
    ssp.path(6)
    ssp.path(5)
