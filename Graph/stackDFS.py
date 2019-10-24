"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: stackDFS.py
@time: 2019/10/24 20:09
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):

    def __init__(self, top = None):
        self.top = top

    def push(self,data):
        #创建新的节点放到栈顶
        self.top = Node(data, self.top)

    def pop(self):
        #拿出栈顶元素，原来的栈发生改变
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        #查看栈顶元素，原来的栈不变
        return self.top.data if self.top is not None else None

    def isEmpty(self):
        return self.peek() is None



class stackDFS:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None
        self.__pre = [] # 深度遍历
        with open(filename) as f:
            line_num = 0  # 第一行是顶点数和边数
            for line in f:
                if line_num == 0:
                    v, e = line.strip().split()
                    self.V = int(v)
                    self.E = int(e)
                    self.adj = [[] for i in range(self.V)]  # 创建二维数组即邻接表
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
        # 对每个顶点进行遍历
        for i in range(self.V):
            if self.__visited[i] == False:
                self.graph_stack_DFS(i)


    def graph_stack_DFS(self, v):
        stack = Stack()


        # 将v压入栈中，标记v顶点已经访问过
        stack.push(v)
        self.__visited[v] = True

        # 循环遍历取出栈中的元素
        while stack.isEmpty() == False:

            # 从栈顶取出元素
            cur = stack.pop()
            self.__pre.append(cur)

            # 对cur的相邻的未遍历过的顶点，分别将它们压入栈中，并做标记
            for w in self.adj[cur]:
                # 查看cur的相邻顶点w是否被遍历过了
                if self.__visited[w] == False:
                    # 此时说明未被遍历过，将w压入栈中
                    stack.push(w)
                    # 维护visited数组，标记w已经被访问过
                    self.__visited[w] = True

    def get_dfs_order(self):
        print("深度优先遍历（非递归实现）：{}".format(self.__pre))

if __name__ == '__main__':
    SDFS = stackDFS("../g_ssp.txt")
    SDFS.get_dfs_order()
