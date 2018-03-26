# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 08:31:53 2018
https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/
https://www.geeksforgeeks.org/applications-of-depth-first-search/
https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
https://www.geeksforgeeks.org/maximum-bipartite-matching/
@author: Siva
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList= defaultdict(list)
        
    
    def addEdge(self,v1,v2):
        self.adjList[v1].append(v2);
    
    def verticecount(self):
        sumvertice=0
        visited = {key: False for key in self.adjList.keys()}
        for k in self.adjList.keys():
            sumvertice=sumvertice + len(self.adjList[k])
            visited.update({k:False for k in self.adjList[k]})
        return sumvertice,visited
        
    def BFSUtil(self,visited,unvisitedvertex):
        q= []
       # visited = [False]*self.verticecount()        
        q.append(unvisitedvertex);
        visited[unvisitedvertex]=True
        while q:
            curvertice=q.pop(0)
            print(curvertice)
            for vertice in self.adjList[curvertice]:
                if(visited[vertice]==False):
                    q.append(vertice)
                    visited[vertice]=True
          #          print(vertice)
          
    def BFS(self,data=None):
        a,visited=self.verticecount()
       # print(visited)
        for k in visited:
             if(visited[k]==False):
                 self.BFSUtil(visited,k)       
                 
    def DFS(self,data=None):
        a,visited=self.verticecount()
      #  print(visited)
        for k in visited:
            if(visited[k]==False):
                self.DFSUtil(k,visited)

        
    def DFSUtil(self,curvertice,visited):
        print(curvertice)
        visited[curvertice]=True
        for vertice in self.adjList[curvertice]:
            if(visited[vertice]==False):                        
                self.DFSUtil(vertice,visited)        

    def topologicalsort(self,data=None):
        a,visited=self.verticecount()
        stack=[]  
      #  print(visited)
        for k in visited:
            if(visited[k]==False):
                self.topologicalUtil(k,visited, stack)
        while stack:
            print(stack.pop())
        
    def topologicalUtil(self,curvertice,visited, stack):        
        visited[curvertice]=True
        for vertice in self.adjList[curvertice]:
            if(visited[vertice]==False):          
                self.topologicalUtil(vertice,visited, stack)     
        stack.append(curvertice)
        
if __name__=='__main__':
    g = Graph()
#==============================================================================
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 3)
#==============================================================================
    g.addEdge('5','11')
    g.addEdge('7','8')
    g.addEdge('3','8')
    g.addEdge('7','11')
    g.addEdge('11','2')
    g.addEdge('11','9')
    g.addEdge('11','10')
    g.addEdge('8','9')
    g.addEdge('3','10')
    print(g.adjList.items())
   # print("Vertices in graph:",g.verticecount())
    print("BFS:")
    g.BFS()
    print("DFS:")
    g.DFS()
    print("Topological Order:")
    g.topologicalsort()
    
