## 一、介绍

### 1.简介
Graph theory algorithm python implementation，which has the base class of the adjacency matrix of the graph and the ajdacency table,depth-first search (pre-order and post-order) and breadth-first search, in addition to the implementation of various application aspect of the graph ,Hamiltonian graph, directed graph Algorithm, the shortest path algorithm, Euler loop and Euler path, network flow, matching problem, etc. 

图论算法python实现，封装了图的邻接矩阵和邻接表的基础类，实现深度优先搜索（前序和后序）和广度优先搜索，图的各种应用方面的实现，哈密顿图，有向图算法，最短路径算法，欧拉回路和欧拉路径，网络流，匹配问题等等

主要是我最近在推荐算法或者nlp的时候，遇到有不懂的，正在系统学习了一下图论，并实现一下

### 2.环境

> python3

## 二、使用介绍

### 1. 图的表示和DFS

#### 1.1. 图的邻接矩阵使用
在AdjacencyMatrix类中

    加载g.txt，初始化图模型
    adjm = AdjList("../g.txt")
    获取图的信息
    adjm.get_graph_information()
    是否存在某条边
    print(adjm.hasEdge(0,4))
    求某个顶点的度
    print(adjm.degree(1))
    深度优先遍历(返回前序和后序遍历) PS：对于图来说无中序遍历，中序遍历只针对二叉树而言
    print(adjm.graphDFS())

#### 1.2. 图的邻接表使用
在AdjacencyList类中

    加载g.txt，初始化图模型
    adjl = AdjList("../g.txt")
    获取图的信息
    adjl.get_graph_information()
    是否存在某条边
    print(adjl.hasEdge(0,4))
    求某个顶点的度
    print(adjl.degree(1))
    深度优先遍历(返回前序和后序遍历) PS：对于图来说无中序遍历，中序遍历只针对二叉树而言
    print(adjl.graphDFS())

### 2. DFS的应用

#### 2.1 联通分量的个数
在一个社交网络的图模型中，求社交团体的个数相当于联通分量的个数
在CC类中    

    获取联通分量个数
    adjl.get_cccount()
    
#### 2.2 单源路径问题
两个顶点若均存在于某一个联通分量中，说明两点之间一定存在路径
在SingleSourcePath类中

    ssp = SingleSourcePath("../g_unconnected.txt", 0)
    ssp.get_graph_information()
    ssp.path(6)

提供第二种实现方法，丢弃负责记录访问顶点的记录的**visited**数组，只使用**pre**数组，节省空间，但相应地减少了代码的可读性

    ssp = SingleSourcePath_v2("../g_ssp.txt", 0)
    ssp.get_graph_information()
    ssp.path(6)
    ssp.path(5)

#### 2.3 无向图的环检测

判断是否有环：
1. 结点v已经访问过
2. 结点w能到结点v
3. 结点w的上一个结点parent不是v


        CD = CycleDetection("../g_cycle.txt")
        CD.get_graph_information()
        CD.hasCycle()
        print("=======第二种========")
        CD2 = CycleDetection_v2("../g_cycle.txt")
        CD2.get_graph_information()
        CD2.hasCycle()
        
#### 2.4 二分图的检测
BiPartitionDetection中，使用染色问题求解

    BPD = BiPartitionDetection("../g.txt")
    BPD.get_graph_information()
    print(BPD.graphDFS())
    print(BPD.isBiPartite())
      
#### 2.5 DFS的非递归
stackDFS类中

    SDFS = stackDFS("../g_ssp.txt")
    SDFS.get_dfs_order()  
    
    
### 3. 广度优先遍历

#### 2.1 BFS

BFS类中,和树的广度优先遍历类似，区别在于图的广度优先遍历需要记录每个节点是否被遍历过，防止有环干扰
其中实现使用了队列queue

    bfs = GraphBFS("../g.txt")
    bfs.get_graph_information()
    bfs.get_BFSorder()
    
> PS：此处可以注意到dfs和bfs的在非递归实现的相同之处,除了使用不同的数据结构存放遍历过程的数据外，其他基本相同
 
     visited[0 .... v-1] = false
     for v in range(self.V):
       if visited[v] == False:   
           search(v)
    
     search(s):
       x.push(s)
       visited[s] = True
       while !x.isEmplty():
           v = x.pop()
           for w in self.adj[w]:
               if visited[w] == False:
                   x.push(w)
                   visited[w] = True
                   
> 此处当x为栈时，为广度优先遍历，为队列的时候为深度优先遍历，除此之外还可以是随机队列等其他数据结构，发挥不同的作用

#### 2.2 环检测
CycleDetection类中

    cd = CycleDetection("../g_cycle.txt")
    print(cd.get_hasCycle())
    
#### 2.3 单源路径
SingleSourcePath类中

    ssp = SingleSourcePath("../g_ssp.txt", 0)
    ssp.get_graph_information()
    ssp.path(4)
    
#### 2.4 二部图检测
BiPartitionDetection类中

    print("=====first graph======")
    g = BiPartitionDetection("g.txt")
    print(g.isBiPartite())
    print("=====second graph======")
    g = BiPartitionDetection("g2.txt")
    print(g.isBiPartite())
    print("=====third graph======")
    g = BiPartitionDetection("g3.txt")
    print(g.isBiPartite())

#### 2.5 最短路径（注意！此处是无向无权图）
USSSPath类中

    usssp = USSSPath("../g_ssp.txt", 0)
    usssp.get_graph_information()
    usssp.path(6)
    usssp.dis(6)
