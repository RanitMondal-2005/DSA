# HEAP without using heapq module 
# LETS make a manual min heap ( MIN PRIORITY QUEUE)

# Main Heap property is -> 
# insert() and delete() -> o(log n), peek()-> o(1),, no matter what u should follow this
class MinHeap:
    def __init__(self):
        self.heap=[]
    # Those three helper functions — parent(), left_child(), and right_child() — are used because although we represent the heap as a linear list, conceptually it’s a binary tree.
    # Since it’s a complete binary tree (always filled level by level, left to right), we can map parent/child relationships using simple index formulas instead of storing actual node pointers like in a linked tree.
    # Here’s the mapping:
    # Parent of node at index i → (i - 1) // 2
    # Left child of node at index i → (2 * i) + 1
    # Right child of node at index i → (2 * i) + 2
    def parent(self,i):
        return (i-1)//2
    
    def left_child(self,i):
        return(2*i)+1
    
    def right_child(self,i):
        return(2*i)+2
    
    # NOTE-> These 3 heper funcs:-
    # 👉 They don’t return the value stored in the heap.
    # 👉 They return the index (position in the list) where that parent/child lives.

    def insert(self,key):
        # simply insert at end
        self.heap.append(key)
        # call heapify Up 
        self.heapifyUp(len(self.heap)-1)


    def heapifyUp(self,i): # bottom -> top
        # fix the heap up (it will maintain heap property even after insertion of a new element)
        while i>0 and self.heap[i]<self.heap[self.parent(i)]:
            p=self.parent(i)
            # swap element at index i with  its parent
            self.heap[i],self.heap[p]=self.heap[p],self.heap[i]
            i=p

    def delete(self): 
        if len(self.heap)==0:
            print("Heap is Empty")
            return
        # we will not directly remove the root , as this will shift all element in left->o(n) due to pop(),, but we need to have log n
        # step 1 -> replace the root with last element of the tree
        last_element=self.heap.pop()
        # now if heap had only 1 element, now it's empty
        if len(self.heap)==0:
            return 
        # step 2 -> assign the last element to root
        self.heap[0]=last_element
        # step 3-> call heapifyDown from root -> leaf
        self.heapifyDown(0)


    def heapifyDown(self,i):# top-> bottom
        n=len(self.heap)
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)
        if left < n and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < n and self.heap[right] < self.heap[min_index]:
            min_index = right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.heapifyDown(min_index)


    def display(self):
        print(self.heap)
    
    def get_min(self):
        if len(self.heap)==0:
            return None
        # as its a min heap so  smallest element always at root
        return self.heap[0]

    def length(self):
        return len(self.heap)

h = MinHeap()
