"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: CycleDetection.py
@time: 2019/10/24 21:18
"""
import queue
class CycleDetection:

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

        self.visited = [False for i in range(self.V)]
        self.pre = [-1 for i in range(self.V)] # 记录每一个结点的父亲结点即上一个结点
        self.hasCycle = False

        # 对每一个结点都进行遍历
        for v in range(self.V):
            # 若该结点为未被访问过，即二部图的情况
            if self.visited[v] == False:
                if self.bfs(v) == True:
                    self.hasCycle = True
                    break


    def bfs(self, s):
        que = queue.Queue(self.V)
        que.put(s)
        self.visited[s] = True
        self.pre[s] = s

        while que.empty() == False:
            v = que.get()

            # 将v的每一个未访问的相邻结点w都压入队列
            for w in self.adj[v]:
                if self.visited[w] == False:
                    que.put(w)
                    self.visited[w] = True
                    self.pre[w] = v
                elif self.pre[v] != w:
                    # 此处是检测环的关键，如果w被访问过了，要检测w是不是上一个结点v，如果不是，则有环
                    return True

    def get_hasCycle(self):
        return self.hasCycle
if __name__ == '__main__':
    cd = CycleDetection("../g_cycle.txt")
    print(cd.get_hasCycle())
