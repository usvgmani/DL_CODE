# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:32:03 2018
1) Create a set mstSet that keeps track of vertices already included in MST.
2) Assign a key value to all vertices in the input graph. 
Initialize all key values as INFINITE. 
Assign key value as 0 for the first vertex so that it is picked first.
3) While mstSet doesn’t include all vertices
….a) Pick a vertex u which is not there in mstSet and has minimum key value.
….b) Include u to mstSet.
….c) Update key value of all adjacent vertices of u. 
    To update the key values, iterate through all adjacent vertices. 
    For every adjacent vertex v, 
        if weight of edge u-v is less than the previous key value of v, 
            update the key value as weight of u-v
@author: siva
"""
import sys
class MSTGraph:
    def __init__(self,v):
        self.vertices=v
        self.adjmatrix=[[0 for cols in range(v) ] for rows in range(v)]
                         
    def printGraph(self):
          for cols in range(self.vertices) :
              for rows in range(self.vertices):
                  if self.adjmatrix[cols][rows] > 0:
                      print("edge(u=",cols,",","v=",rows,
                                  "weight=",self.adjmatrix[cols][rows],")")  
    def minKey(self,mstSet,keys):
        #get all adj elements and get minimum weight
        minweight=sys.maxsize
        nextu=-1
        for i in range(self.vertices):
            if(keys[i]<minweight and mstSet[i]==False):
                minweight=keys[i]
                nextu=i
        return nextu        

    def printMST(self,parent):
        for k in range(1,self.vertices):
            print("edge(u=",parent[k],",","v=",k,
            "weight=",self.adjmatrix[parent[k]][k],")")
            
    def primMST(self):
        keys=[sys.maxsize for k in range(self.vertices)]   
        mstSet=[False]*self.vertices
        parent=[-1]*self.vertices                   
        keys[0]=0        
        for cout in range(self.vertices):            
            minadjvertice=self.minKey(mstSet,keys)            
            mstSet[minadjvertice]=True
            for k in range(self.vertices):
                if(self.adjmatrix[minadjvertice][k] > 0 
                   and self.adjmatrix[minadjvertice][k]<keys[k]
                   and mstSet[k]==False):
                    keys[k] = self.adjmatrix[minadjvertice][k]
                    parent[k]=minadjvertice
                                       
        self.printMST(parent)
        
if __name__=='__main__':
    g= MSTGraph(5)

    
    g.adjmatrix = [ [0, 2, 0, 6, 0],
                    [2, 0, 3, 8, 5],
                    [0, 3, 0, 0, 7],
                    [6, 8, 0, 0, 9],
                    [0, 5, 7, 9, 0],
           ]
    print(g.adjmatrix)
    g.printGraph()
    print("MST:")
    g.primMST()
