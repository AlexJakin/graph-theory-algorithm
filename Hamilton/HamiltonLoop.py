"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: HamiltonLoop.py
@time: 2019/10/20 19:12
"""
class HamiltonLoop:

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
        self.__visited = [False for i in range(self.V)]
        self.__pre = [-1 for i in range(self.V)]
        self.__end = -1
        self.graphDFS(0,0)

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

    def allVisited(self):
        for v in range(self.V):
            if self.__visited[v] == False:
                return False
        return True

    def graphDFS(self, v, parent):

        # 标记v顶点已经遍历过了
        self.__visited[v] = True
        # 记录父亲结点
        self.__pre[v] = parent

        for w in self.adj[v]:
            if self.__visited[w] == False:
                if self.graphDFS(w, v):
                    return True
            elif w == 0 and self.allVisited():
                # 记录到达的最后一个结点
                self.__end = v
                return True
        # 找不到HamiltonLoop，开始回溯到上一个结点
        self.__visited[v] = False
        return False

    def getHamiltonLoop(self):
        res = []
        if self.__end == -1:
            return res

        cur = self.__end
        while cur != 0:
            res.append(cur)
            cur = self.__pre[cur]
        res.append(0)
        res.reverse()
        print(res)

if __name__ == '__main__':
    hl = HamiltonLoop("g.txt")
    hl.get_graph_information()
    hl.getHamiltonLoop()

    hl = HamiltonLoop("g2.txt")
    hl.get_graph_information()
    hl.getHamiltonLoop()
