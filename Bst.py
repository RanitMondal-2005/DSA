# Implementing a Binary search Tree in Python
# BST Property->
# All nodes at left are smaller than parent ,and all nodes at right are greater than parent
# another property - if we do inorder traversal(left->root->right)in BST we will get tree in sorted order(ASCENDING FORM)
from que import Queue 
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
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
                key=int(input("enter node to delete: "))
                self.deletion(self.root,key)
            case 3:
                self.searching(self.root)
            case 4:
                self.display()
            case 5:
                print("Height of the Binary Search tree is=",self.height(self.root))
            case 6:
                self.traversal()
            case 7:
                print("Balanced Binary Search Tree?",self.check_balanced_bst())
            case 8:
                exit()
            case _:
                print("invalid choice")
         self.menu()

    def insertion(self):
        # REMEMBER -> the new node value does not exist in the original BST(no repeat)
        num=int(input("enter data to insert:"))
        newnode=TreeNode(num)
        # case 1
        if self.root is None: # 1st element to insert
            self.root=newnode
            return 
        # case 2
        # if element < root , put in left subtree , else put in right subtree
        curr=self.root
        while curr:
           if newnode.val<curr.val: # put left
               if curr.left is not None:
                 curr=curr.left
               else: # none paye gale, left aa faka
                 curr.left=newnode
                 return 
           if newnode.val>curr.val: # put right
               if curr.right is not None:
                   curr=curr.right
               else:
                   curr.right=newnode
                   return 


    def deletion(self,root,key):
        x=sum(self.traversal(),[]) # flatten list
        if key not in x:
            print("Node not present in Tree")
            return
        
        # recursive solution

        if root is None: # base case
            return None
        
        if root.val>key: # move left
            # 1st delete then assign it to the original tree backk
            root.left=self.deletion(root.left,key)

        if root.val<key: # move right
            # 1st delete then assign it to the original tree backk
            root.right=self.deletion(root.right,key)

        else: # key==root.val
            # here comes 3 cases 
            # case 1 -> deleting leaf nodes , direct delete
            if root.left is None and root.right is None:
                return None
            # case 2-> deleting a node which has only 1 child , simply delete that node and link the rest tree with its only child
            elif root.left is None: # child at right
                return root.right # link tree with right
            elif root.left is None: # child at left
                return root.right # link tree with left
            #case 3-> deleting node has both childs present
            else: 
                # then find in-order successor of the node, replace with that and delete that
                # RULE= inorder successor of a node will always be present in its right subtree's left most node
                temp=root.right
                while temp.left is not None:
                    temp=temp.left
                # assign
                root.val=temp.val
                # temp is leaf node, and it is present in right so simply delete it like prev
                root.right=self.deletion(root.right,temp.val)
        return root

    def searching(self,root):
        if root is None:
            print("Tree empty")
            return     
        target=int(input("enter node to search="))
        curr=root
        while curr:
            if curr.val==target:
                print("target found")
                return 
            elif target<curr.val:
                curr=curr.left
            else:
                curr=curr.right
        print("Node not found")
        return 
    
    def traversal(self):
        # level order traversal
        if self.root is None:
            print("Tree empty")
            return
        queue=Queue()
        ans=[]
        ans.append([self.root.val])
        queue.enqueue(self.root)
        while queue.length()>0:  
            level=[]
            l=queue.length()
            for _ in range(l):  
                front=queue.dequeue()
                if front.left is not None:
                    queue.enqueue(front.left)
                    level.append(front.left.val)
                if front.right is not None:
                    queue.enqueue(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                ans.append(level)
        return ans

    def display(self):
        if self.root is None:
            print("tree empty")
            return 
        print("traversal ->", self.traversal())

    def height(self,root):
        # height of Bst 
        if root is None:
            return 0
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        if abs(left_height-right_height)>1:
            self.ans=False
        return 1+max(left_height,right_height)
    
    def check_balanced_bst(self):
        self.ans=True
        self.height(self.root)
        return self.ans
    
bst1=BST()