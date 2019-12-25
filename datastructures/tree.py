class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # constructs a Tree from a List
    def from_list(self, l):
        raise NotImplemented()

    # converts a Tree into a List
    def to_list(self):
        raise NotImplemented()
