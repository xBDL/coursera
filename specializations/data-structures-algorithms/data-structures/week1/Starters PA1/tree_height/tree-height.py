# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = 5 #int(sys.stdin.readline())
                self.parent = [4, -1, 4, 1, 1] #list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
 
                height = 0
                heights = [-1]*self.n
                print('heights are ' + str(heights))

                root = self.parent.index(-1)
                heights[root] = height
                print('root is ' + str(root))
                print('heights are ' + str(heights))                

                children = [i for i, x in enumerate(self.parent) if x == root]
                print('children are ' + str(children))
                
                height += 1                
                
                for child in children:
                    heights[child] = height
                    print('heights are ' + str(heights))                    
                    children = [i for i, x in enumerate(self.parent) if x == child]
                    print('children are ' + str(children))
                    
        
        
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
