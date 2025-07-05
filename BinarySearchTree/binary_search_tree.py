class NewNode:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insertion_in_bst(self, data):
        """To insert the data in BST"""
        self.root = self.recursiv_insertion(self.root, data)

    def recursiv_insertion(self, root, data):
        if root is None:
            return NewNode(item=data)
        if root.item > data:
            root.left = self.recursiv_insertion(root.left, data)
        elif root.item < data:
            root.right = self.recursiv_insertion(root.right, data)
        return root
    
    def insertion_without_recursion(self, data):
        """Insert node in BST without recursion approach"""
        if self.is_empty():
            self.root = NewNode(item=data)
        else:
            temp = self.root
            parent = None
            while temp is not None:
                parent = temp
                if temp.item > data:
                    temp = temp.left
                elif temp.item < data:
                    temp = temp.right
            if parent.item > data:
                parent.left = NewNode(item=data)
            else:
                parent.right = NewNode(item=data)
   
    def search(self, data):
        """To search the data in BST"""
        if self.is_empty():
            print("BST is empty.")
            return
        temp = self.root
        while temp is not None:
            if temp.item == data:
                print("Data found in BST ::", temp.item)
                return temp
            elif temp.item > data:
                temp = temp.left
            else:
                temp = temp.right
        print("Data not found in BST.")
                
    def preorder_traversing(self):
        """To traverse through each node in BST"""
        result = []
        self.recur_preorder_traversing(self.root, result)
        return result
        
    def recur_preorder_traversing(self, root, result):
        """Recursive Function for Preorder traversing"""
        if root:
            result.append(root.item)
            self.recur_preorder_traversing(root.left, result)
            self.recur_preorder_traversing(root.right, result)

    def inorder_traversing(self):
        """To traverse through each node in BST"""
        result = []
        self.recur_inorder_traversing(self.root, result)
        return result
        
    def recur_inorder_traversing(self, root, result):
        """Recursive Function for Inorder traversing"""
        if root:
            self.recur_inorder_traversing(root.left, result)
            result.append(root.item)
            self.recur_inorder_traversing(root.right, result)
        
    def postorder_traversing(self):
        """To traverse through each node in BST"""
        result = []
        self.recur_postorder_traversing(self.root, result)
        return result
        
    def recur_postorder_traversing(self, root, result):
        """Recursive Function for Postorder traversing"""
        if root:
            self.recur_postorder_traversing(root.left, result)
            self.recur_postorder_traversing(root.right, result)
            result.append(root.item)
            
    def minimum_value_in_bst(self):
        """To retrive the minimum value of the bst"""
        if self.is_empty():
           return 
        temp = self.root
        min_val = 0
        while temp is not None:
            min_val = temp.item
            temp = temp.left
        return min_val
    
    def maximum_value_in_bst(self):
        """To retrive the maximum value of the bst"""
        if self.is_empty():
           return 
        temp = self.root
        max_val = 0
        while temp is not None:
            max_val = temp.item
            temp = temp.right
        return max_val
    
    def size_of_bst(self):
        """Return the size (number of nodes) of BST without recursion"""
        if self.root is None:
            print("Size of BST :: 0")
            return 0
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        print("Size of BST ::", count)
        return count
        
    def deletion_of_node_in_bst(self, data):
        """To delete the node from BST"""
        if not self.is_empty():
            temp = self.root
            parent= None
            while temp is not None:
                if temp.item == data:
                    break
                elif temp.item > data:
                    parent = temp
                    temp = temp.left
                else:
                    parent = temp
                    temp = temp.right
            print("item",temp.item)
            if temp.left == None:
                parent.left = temp.right
            elif temp.right == None:
                parent.left = temp.left
            else:
                # Find the in-order predecessor (max in left subtree)
                pred_parent = temp
                pred = temp.left
                while pred.right:
                    pred_parent = pred
                    pred = pred.right
                temp.item = pred.item  # Replace value
                # Delete the predecessor node
                if pred_parent == temp:
                    pred_parent.left = pred.left
                else:
                    pred_parent.right = pred.left
            


bst = BinarySearchTree()
bst.insertion_in_bst(50)
bst.insertion_in_bst(20)
bst.insertion_in_bst(25)
bst.insertion_in_bst(15)
bst.insertion_in_bst(70)
bst.insertion_in_bst(75)
bst.insertion_in_bst(65)
bst.insertion_without_recursion(40)
bst.insertion_without_recursion(30)
bst.insertion_without_recursion(85)
bst.insertion_without_recursion(60)
bst.search(65)
print("BST Tree PreOrder",bst.preorder_traversing())
print("BST Tree InOrder",bst.inorder_traversing())
print("BST Tree PostOrder",bst.postorder_traversing())
print("Min value of BST ::",bst.minimum_value_in_bst())
print("Max value of BST ::",bst.maximum_value_in_bst())
print("Size of BST ::",bst.size_of_bst())
bst.deletion_of_node_in_bst(70)
print("Size of BST ::",bst.size_of_bst())
print("BST Tree InOrder",bst.inorder_traversing())