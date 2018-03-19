# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:22:15 2018

"""
import numpy as np
import collections as col

class Node:
    def __init__(self,data):
        self.payload=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=root
        self.leaflist=[]
    
    def inorder(self,node):
        #LrR
        if(node==None):
            return 
        self.inorder(node.left)
        print(node.payload)
        self.inorder(node.right)
        
    def postorder(self,node):
        #rLR
        if(node==None):
            return 
        print(node.payload)    
        self.postorder(node.left)
        self.postorder(node.right)
        
    def preorder(self,node):
        #LRr
        if(node==None):
            return   
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.payload)  
    
    def maxnodesatlevel(self,level):
        #number of levels
        return np.pow(2,level-1)
    
    def maxnodesintree(self,height):
        #height
        return np.pow(2,height)-1

    def leafnodes(self,node):
        if(node==None):
            return
        if(node.left==None and node.right==None and node!=None):
            self.leaflist.append(node.payload)         
            print(node.payload)
        self.leafnodes(node.left)
        self.leafnodes(node.right)    
        
    def buildtree(self,levelorderlst):
        dq=col.deque(levelorderlst)
        treeq=col.deque()
        self.root=Node(dq.popleft())
        treeq.appendleft(self.root)
        while(treeq):
            anode=treeq.pop()    
            if(not dq): return
            leftchild=Node(dq.popleft())
            if(leftchild is None): return
            anode.left=leftchild
            
            if(not dq): return
            rightchild=Node(dq.popleft())
            if(rightchild is None): return                        
            anode.right=rightchild
            
            treeq.appendleft(leftchild)
            treeq.appendleft(rightchild)

    def countNodes(self,root):
        if root is None:
            return 0
        return (1+ self.countNodes(root.left) + self.countNodes(root.right))
     
    def isComplete(self,root, index, number_nodes):         
        if root is None:
            return True
        if index >= number_nodes :
            return False
        return (self.isComplete(root.left , 2*index+1 , number_nodes)
            and self.isComplete(root.right, 2*index+2, number_nodes))
        
    def boundaryleft(self,node):
        #topdown
        if(node==None):
            return
        if(node.left):    
            print(node.payload)  
            self.boundaryleft(node.left)
        elif(node.right):
            print(node.payload)
            self.boundaryleft(node.right)
            
    def boundaryright(self,node):
        #bottomup
        if(node==None):
            return
        if(node.right):      
            self.boundaryright(node.right)
            print(node.payload) 
        elif(node.left):
            self.boundaryright(node.left) 
            print(node.payload)
    
    def printboundary(self,node):
        if(node==None):
            return
        self.boundaryleft(node.left)
        self.leafnodes(node.left)        
        self.leafnodes(node.right)
        self.boundaryright(node.right)        
        
    def levelorder(self,height):
        for i in range(1,height):
            self.currentlevelnodes(self.root,i)
            print("")
            
    def  currentlevelnodes(self,node,level):
        if(node==None): return
        if(level==1):
            print("-",node.payload,"-", end="", flush=True)
        else:
            self.currentlevelnodes(node.left,level-1)
            self.currentlevelnodes(node.right,level-1)
             
if __name__=='__main__':
    tree=BinaryTree(None)
    arr=np.arange(1, 21)
    np.random.shuffle(arr)
    print(arr)
    tree.buildtree(arr)
    print("Inorder")
    tree.inorder(tree.root)
    print("Preorder")
    tree.preorder(tree.root)
    print("Postorder")
    tree.postorder(tree.root)
    print("leafnodes")
    tree.leafnodes(tree.root)
    print(tree.leaflist)
    print("No of Leaf Nodes:",len(tree.leaflist))
    print("No of Levels:",np.rint(np.log2(len(tree.leaflist))))
    print("No of nodes with 2 children:",(len(tree.leaflist)-1))
    node_count=tree.countNodes(tree.root)
    print("No of nodes:",node_count)
    print("Binary Tree is Complete? ",tree.isComplete(tree.root,0,node_count))
    print("The boundary list:")
    print(tree.root.payload)
    tree.printboundary(tree.root)
    print("Level order list:")
    tree.levelorder(int(np.rint(np.log2(len(tree.leaflist)))+1))
    
