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
                    
    def search(self, data):
        """To search the data in BST"""
        if self.is_empty():
            print("BST is empty.")
            return
        temp = self.root
        while temp is not None:
            if temp.item == data:
                print("Data found in BST ::", temp.item)
                return
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
            


bst = BinarySearchTree()
bst.insertion_in_bst(50)
bst.insertion_in_bst(20)
bst.insertion_in_bst(25)
bst.insertion_in_bst(15)
bst.insertion_in_bst(70)
bst.insertion_in_bst(75)
bst.insertion_in_bst(65)
bst.search(65)
print("BST Tree PreOrder",bst.preorder_traversing())
print("BST Tree InOrder",bst.inorder_traversing())
print("BST Tree PostOrder",bst.postorder_traversing())