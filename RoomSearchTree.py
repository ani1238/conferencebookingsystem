class TreeNode:
    def __init__(self):
        self.rooms = []
        self.children = []
        self.isLeaf = True


class RoomSearchTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, room):
        self._insert(self.root, room)

    def _insert(self, node, room):
        if node.isLeaf:
            node.rooms.append(room)
            if len(node.rooms) > 3:  # Adjust this threshold as needed
                self._split_node(node)
        else:
            child = self._find_appropriate_child(node, room)
            self._insert(child, room)

    def _find_appropriate_child(self, node, room):

        return node.children[0]  # Simplified: always choose the first child.

    def _split_node(self, node):

        left = TreeNode()
        right = TreeNode()
        left.rooms.extend(node.rooms[0:2])
        right.rooms.extend(node.rooms[2:3])
        node.rooms.clear()
        node.children.extend([left, right])
        node.isLeaf = False

    def search_rooms(self, search_strategy):
        results = []
        self._search(self.root, results, search_strategy)
        return results

    def _search(self, node, results, search_strategy):
        if node.isLeaf:
            results.extend(search_strategy.search(node.rooms))
        else:
            for child in node.children:
                self._search(child, results, search_strategy)
