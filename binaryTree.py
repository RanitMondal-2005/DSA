# Creating a simple Binary Tree with basic operations
class Queue:
    # basic queue _ list implementation
    def __init__(self):
        self.l=[]    
    def enqueue(self,num): # PUSH
        return self.l.append(num)
    def dequeue(self): # DELETE
        if len(self.l)==0:
            return -1 # no element
        return self.l.pop(0)
    def length(self):
        x=len(self.l)
        return x
    
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
        self.ans=True
        self.menu()
    def menu(self):
        x=int(input("enter your choice :"))
        match x:
            case 1:
                self.insertion()
            case 2:
                self.deletion()
            case 3:
                self.searching()
            case 4:
                self.display()
            case 5:
                print("Height os the Binary tree is=",self.height(self.root))
            case 6:
                self.traversal()
            case 7:
                print("Balanced Binary Tree?",self.check_balanced_binary_tree())
            case 8:
                exit()
            case _:
                print("invalid choice")
        self.menu()


    def insertion(self):
        # Rule of insertion in Binary Tree is:
        # do level order traversal , enter in the 1st empty slot found in the tree
        data=int(input("enter your node's value to be inserted:"))
        newnode=TreeNode(data)
        # if tree was empty
        if self.root is None:
           self.root=newnode
           return
        # if already tree existed
        # find 1st empty slot using level order traversal logic
        queue=Queue()
        queue.enqueue(self.root)
        while queue.length()>0:
            front=queue.dequeue()
            if front.left is not None:
                queue.enqueue(front.left)
            else: 
                front.left=newnode
                return 
            if front.right is not None:
                queue.enqueue(front.right)
            else: 
                front.right=newnode
                return
    # in insertion we don’t actually need levels, 
    # we only need to find the first empty spot (left → right order), that's it,
    # so queue is storing each nodes one by one , who cares,
    
    def deletion(self):
        # Case 1: Tree
        if self.root is None:
            print("Empty tree, deletion not possible")
            return
        # if tree had nodes, then the rule of deletion in a binary tree:
        # find the node to be deleted , replace the node with its child then delete that child
        # Case 2:
        # if only root is present in the Binary Tree
        key = int(input("Enter which node to delete: "))
        if self.root.left is None and self.root.right is None:
            if self.root.val == key:
                self.root=None
                print("Root deleted")
                return
            else:
                print("key not found")
                return
        # Case 3:
        # if root has more than 1 child
        # level order traversal to find target and deepest node
        nodes = self.traversal(return_nodes=True) 
        all_nodes=sum(nodes,[]) # flatten list
        # all nodes will be a single list having all nodes in the Tree
        node_to_delete = None
        last_node = None
        for n in all_nodes:
           if n.val == key:
             node_to_delete = n
           last_node = n   # keep updating -> at the end, this will be deepest node
        # node_to_delete → reference to the node whose value = key.
        # last_node → keeps updating in loop, so at the end it’s the deepest, last node in BFS.
        if node_to_delete is None:
             print("Node not found")
             return
        # replace value
        node_to_delete.val = last_node.val
        # delete deepest node
        for n in all_nodes:
         if n.left == last_node:
             n.left = None
             break
         if n.right == last_node:
             n.right = None
             break

          

    def searching(self):
        target=int(input("enter a node to search="))
        elements=sum(self.traversal(), [])  # flatten list
        if len(elements)==0:
            print("Tree empty")   
        elif target in elements:
            print("Target found")
        else:
            print("Target not found")

    def display(self):
        # same use level order travsersal or any traversal
        if self.root is None:
            print("empty tree")
        else:
            print("Tree Traversal->",self.traversal())

    def height(self,root): # height or max depth or length of the tree
        # using recursive code
        if root is None:
            return 0 # leaf nodes have height 0
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        if abs(left_height-right_height)>1:
            self.ans=False
        return 1+max(left_height,right_height)
    
    def check_balanced_binary_tree(self): 
        # this is a bit useless, cause we are maintaining a complete binaryu tree here
        self.ans=True
        self.height(self.root)
        return self.ans
    
    def traversal(self,return_nodes=False): # to reuse traversal we need to have reference also
        # using level order traversal,for reusability
        queue=Queue()
        ans=[]
        if self.root is None:
            return []
        queue.enqueue(self.root)
        while queue.length()>0:
            level=[]
            l=queue.length()
            for _ in range(l):
                front=queue.dequeue()
                if return_nodes: # if nodes requested, store node ref, else store value
                    level.append(front)
                else:
                    level.append(front.val)
                if front.left is not None:# if nodes requested, store node ref, else store value
                    queue.enqueue(front.left)
                if front.right is not None:
                    queue.enqueue(front.right)
            ans.append(level)
        return ans
        # here we upgraded our traversal() so it can serve two modes:
        # Default mode (values) → like now, returns list of values [[1],[2,3]].
        # Node mode → returns actual TreeNode objects in level order, which we can reuse in deletion.
    
b1=BinaryTree()   