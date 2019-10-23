"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: BiPartitionDetection.py
@time: 2019/10/22 17:50
"""
class BiPartitionDetection:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__isBiPartite = True
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


    def graphDFS(self):
        visited = [False for i in range(self.V)]
        colors = [-1 for i in range(self.V)]

        def dfs(v, color):
            # 标记v顶点已经遍历过了
            visited[v] = True
            for w in self.adj[v]:
                if visited[w] == False:
                    if dfs(w, 1-color) == False:
                        return False
                elif colors[w] == colors[v]:
                    return False

        # 顾及到有多个联通分量，对每个顶点都做DFS
        for i in range(self.V):
            if visited[i] == False:
                if dfs(i, 0) == False:
                    self.__isBiPartite = False
                    break
    def isBiPartite(self):
        return self.__isBiPartite



if __name__ == '__main__':
    BPD = BiPartitionDetection("../g.txt")
    BPD.get_graph_information()
    print(BPD.graphDFS())
    print(BPD.isBiPartite())
