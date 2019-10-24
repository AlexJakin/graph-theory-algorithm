"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: SingSourcePath.py
@time: 2019/10/24 16:53
"""
import queue
class SingleSourcePath:

    def __init__(self, filename, s):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__order = [] # 广度优先遍历
        self.s = s  # 源
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
        self.graphBFS()

    def get_graph_information(self):
        """
        打印图的邻接表
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        for i, v in enumerate(self.adj):
            print("{} : {}".format(i, v))



    def graphBFS(self):
        visited = [False for i in range(self.V)]
        pre = [-1 for i in range(self.V)]
        order = []

        def bfs(v):
            # 使用队列来存放经过结点
            que = queue.Queue(self.V)
            # 经过顶点v时，将v放进队列中
            que.put(v)
            visited[v] = True
            pre[v] = v
            # 队列为空时，即在某个联通分量已经遍历完毕
            while que.empty() == False:
                # 取出v 并做标记将v放入order 后面开始对v的邻点遍历
                v = que.get()
                order.append(v)

                for w in self.adj[v]:
                    if visited[w] == False:
                        que.put(w)
                        visited[w] = True
                        # 将w放入队列的时候 此时上一个结点正是v
                        pre[w] = v

        for i in range(self.V):
            if visited[i] == False:
                bfs(i)
        self.__order = order
        self.__pre = pre

    def isConnectedTo(self, t):
        """
        判断到目标顶点t是否可达
        :param t: 目标
        :return:
        """
        self.validateVertex(t)
        return self.__pre[t]

    def validateVertex(self, v):
        """
        验证顶点取值
        :param v:
        :return:
        """
        if v<0 or v>=self.V:
            raise ValueError("v值超出范围")

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
        print(self.__pre)
        print("{} -> {}的路径为：{}".format(self.s, t, res))

if __name__ == '__main__':
    ssp = SingleSourcePath("../g_ssp.txt", 0)
    ssp.get_graph_information()
    ssp.path(4)
