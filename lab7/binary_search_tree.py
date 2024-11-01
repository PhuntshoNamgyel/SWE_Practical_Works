# Step 1: Define the Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: Implement the Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Step 3: Implement the Insertion Method
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Step 4: Implement the Search Method
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Step 5: Implement Traversal Methods
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # Step 6: Implement the Deletion Method
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    # Step 7: Implement the Method to Find the Maximum Value
    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right is not None:  # Go as far right as possible
            current = current.right
        return current.value  # Return the maximum value found


    # Step 8: Implement the method to count the total number of nodes
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if not node:
            return 0  # Base case: if node is None, there are no nodes to count
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Step 9: Implement the Level-order Traversal Method
    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]  # Start with the root node in the queue

        while queue:
            current_node = queue.pop(0)  # Process nodes in FIFO order
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)  # Add left child to queue if it exists
            if current_node.right:
                queue.append(current_node.right)  # Add right child to queue if it exists

        return result

    # Step 10: Implement the Method to Find the Height of the BST
    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if not node:
            return -1  # Base case: height is -1 if there are no nodes
        left_height = self._find_height_recursive(node.left)  # Recursively find left subtree height
        right_height = self._find_height_recursive(node.right)  # Recursively find right subtree height
        return 1 + max(left_height, right_height)  # Height is 1 + maximum height of left or right subtree

    # Step 11: Implement the Method to Check If the Tree is a Valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if not node:
            return True  # Base case: an empty tree is a valid BST
        if not (min_value < node.value < max_value):  # Validate the current node's value
            return False
        # Recursively check left subtree (values < node.value) and right subtree (values > node.value)
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_value))


# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test search
print(bst.search(4))  # Should return a Node
print(bst.search(9))  # Should return None

# Test traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())

# Test find_max
print("Maximum value in the BST:", bst.find_max())

# Test count_nodes
print("Total number of nodes in the BST:", bst.count_nodes())

# Test level_order_traversal
print("Level-order traversal:", bst.level_order_traversal())

# Test find_height
print("Height of the BST:", bst.find_height())

# Test is_valid_bst
print("Is the BST valid?:", bst.is_valid_bst())
