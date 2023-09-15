from RoomSearchTree import RoomSearchTree


class RoomSearchManager:
    tree = RoomSearchTree()
    # def __init__(self):
    #     tree = RoomSearchTree()

    # _instance = None

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super(RoomSearchManager, cls).__new__(cls)
    #         cls._instance.initialize()
    #     return cls._instance

    @staticmethod
    def add_room_to_tree(room):
        RoomSearchManager.tree.insert(room)

    @staticmethod
    def get_room_search_tree():
        return RoomSearchManager.tree
