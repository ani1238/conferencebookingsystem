from RoomSearchTree import RoomSearchTree


class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.rooms = []

    def get_floor_number(self):
        return self.floor_number

    def add_room(self, room):
        RoomSearchTree.insert(room)
        self.rooms.append(room)

    def get_rooms(self):
        return self.rooms
