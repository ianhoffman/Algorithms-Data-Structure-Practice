class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @property
    def height(self):
        return max(
            self.left.height if self.left else 0,
            self.right.height if self.right else 0
        ) + 1

    @property
    def balance(self):
        return (self.left.height if self.left else 0) - (self.right.height if self.right else 0)

    def get_min_value_node(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def insert(self, key):
        if key <= self.key:
            if self.left is None:
                self.left = AVLTreeNode(key)
            else:
                self.left = self.left.insert(key)
        else:
            if self.right is None:
                self.right = AVLTreeNode(key)
            else:
                self.right = self.right.insert(key)

        balance = self.balance
        if balance > 1:
            if key > self.left.key:  # Left Right Case                        
                self.left = self.left.rotate_left()
            root = self.rotate_right()
        elif balance < -1:
            if key < self.right.key:  # Right Left Case
                self.right = self.right.rotate_right()
            root = self.rotate_left()
        else:
            root = self

        return root

    def delete(self, key):
        if key == self.key:
            if self.left and self.right:
                min_value_node = self.right.get_min_value_node()
                self.key = min_value_node.key
                self.right = self.right.delete(self.key)
                root = self
            else:
                root = self.left or self.right
        else:
            if key < self.key and self.left:
                self.left = self.left.delete(key)
            elif key > self.key and self.right:
                self.right = self.right.delete(key)
            root = self

        if root:
            balance = self.balance
            if balance > 1:  # Left-heavy
                if self.left and self.left.balance < 0:
                    self.left = self.left.rotate_left()
                root = self.rotate_right()
            elif balance < -1:
                if self.right and self.right.balance > 0:
                    self.right = self.right.rotate_right()
                root = self.rotate_left()

        return root

    def rotate_left(self):
        root = self.right
        left_subtree = root.left
        root.left = self
        self.right = left_subtree
        return root

    def rotate_right(self):
        root = self.left
        right_subtree = root.right
        root.right = self
        self.left = right_subtree
        return root

    def print_preorder(self):
        print(self.key, end=' ')
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()


if __name__ == '__main__':
    root = AVLTreeNode(0)
    root = root.insert(1)
    root = root.insert(2)
    root = root.insert(3)
    root = root.insert(4)
    root = root.insert(5)
    root = root.insert(2.2)

    assert root.height == 4
    assert root.key == 3
    assert root.left.key == 1
    assert root.left.right.key == 2
    assert root.left.right.right.key == 2.2
    assert root.left.left.key == 0
    assert root.right.key == 4
    assert root.right.right.key == 5

    root.print_preorder()
    print('')

    root = AVLTreeNode(9)
    root = root.insert(5)
    root = root.insert(10)
    root = root.insert(0)
    root = root.insert(6)
    root = root.insert(11)
    root = root.insert(-1)
    root = root.insert(1)
    root = root.insert(2)

    root = root.delete(10)

    root.print_preorder()



