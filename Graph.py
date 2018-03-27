# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 08:31:53 2018

@author: Siva
https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
https://www.geeksforgeeks.org/maximum-bipartite-matching/
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList= defaultdict(list)
        self.adjWeightedList= defaultdict(list)
            
    def addEdge(self,v1,v2):
        self.adjList[v1].append(v2);

    def addweighedEdge(self,v1,v2,w):
        self.adjWeightedList[v1].append((v2,w));
        self.addEdge(v1,v2)

    def verticecount(self):
        sumvertice=0
        visited = {key: False for key in self.adjList.keys()}
        for k in self.adjList.keys():
            sumvertice=sumvertice + len(self.adjList[k])
            visited.update({k:False for k in self.adjList[k]})
        return sumvertice,visited
        
    def BFSUtil(self,visited,unvisitedvertex,stack):
        q= []       
        q.append(unvisitedvertex);
        visited[unvisitedvertex]=True
        while q:
            curvertice=q.pop(0)
            stack.append(curvertice)
            for vertice in self.adjList[curvertice]:
                if(visited[vertice]==False):
                    q.append(vertice)
                    visited[vertice]=True
          
    def BFS(self,data=None):
        a,visited=self.verticecount()
        stack=[]
        for k in visited:
             if(visited[k]==False):
                 self.BFSUtil(visited,k,stack)       
        return stack
         
    def DFS(self,data=None):
        stack=[]  
        a,visited=self.verticecount()
        if(data is not None):
            self.DFSUtil(data,visited,stack)
            return visited
        else:                
            for k in visited:
                if(visited[k]==False):
                    self.DFSUtil(k,visited,stack)
                    lastvisited=k
            return stack,lastvisited    

        
    def DFSUtil(self,curvertice,visited,stack):
        stack.append(curvertice)    
        visited[curvertice]=True
        for vertice in self.adjList[curvertice]:
            if(visited[vertice]==False):                        
                self.DFSUtil(vertice,visited,stack)        

    def topologicalsort(self,data=None):
        a,visited=self.verticecount()
        stack=[]  
        for k in visited:
            if(visited[k]==False):
                self.topologicalUtil(k,visited, stack)
        print(list(reversed(stack)))
        
    def topologicalUtil(self,curvertice,visited, stack):        
        visited[curvertice]=True
        for vertice in self.adjList[curvertice]:
            if(visited[vertice]==False):          
                self.topologicalUtil(vertice,visited, stack)     
        stack.append(curvertice)
   
    #idea that last node is the Mother    
    def findMother(self):
        a,visited=self.verticecount()
        lastnode,lastvisited=self.DFS() 
        if(lastvisited):
            tempvisited=self.DFS(lastvisited)
            if(any(tempvisited[i]==False for i in tempvisited)):
                return None
            else:
                 return lastvisited
            

if __name__=='__main__':
    g = Graph()
    g.addweighedEdge('r','t',3)
    g.addweighedEdge('r','s',5)
    g.addweighedEdge('t','y',4)
    g.addweighedEdge('t','z',2)
    g.addweighedEdge('t','x',7)
    g.addweighedEdge('x','y',-1)
    g.addweighedEdge('x','z',1)
    g.addweighedEdge('s','x',6)
    g.addweighedEdge('s','t',2)
    g.addweighedEdge('y','z',-2)
#==============================================================================
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 3)
#==============================================================================
#==============================================================================
#     g.addEdge('5','11')
#     g.addEdge('7','8')
#     g.addEdge('3','8')
#     g.addEdge('7','11')
#     g.addEdge('11','2')
#     g.addEdge('11','9')
#     g.addEdge('11','10')
#     g.addEdge('8','9')
#     g.addEdge('3','10')
#==============================================================================
#==============================================================================
#     g.addEdge('0', '1');
#     g.addEdge('0', '2');
#     g.addEdge('1', '3');
#     g.addEdge('4', '1');
#     g.addEdge('6', '4');
#     g.addEdge('5', '6');
#     g.addEdge('5', '2');
#     g.addEdge('6', '0');
#==============================================================================
 
    print(g.adjWeightedList.items())
   # print("Vertices in graph:",g.verticecount())
    print("BFS:")
    print(g.BFS())
    print("DFS:")
    print(g.DFS())
    print("Topological Order:")
    g.topologicalsort()
    print("Find Mother:")
    print("Mother is:",g.findMother())
    
