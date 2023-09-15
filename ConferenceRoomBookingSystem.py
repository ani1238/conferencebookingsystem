from RoomSearchManager import RoomSearchManager
from Floor import Floor
from Room import Room
from Organization import Organization


class ConferenceRoomBookingSystem:
    floors = []

    def __init__(self):
        self.organizations = []

    @staticmethod
    def add_floor(floor_number):
        new_floor = Floor(floor_number)
        ConferenceRoomBookingSystem.floors.append(new_floor)
        print(f"Floor {floor_number} added successfully.")
        return new_floor

    def list_available_rooms(self, start_time, end_time):
        available_rooms = []
        for floor in ConferenceRoomBookingSystem.floors:
            for room in floor.rooms:
                if room.is_available(start_time, end_time):
                    available_rooms.append(room)
        return available_rooms

    def add_organization(self, organization_name):
        new_organization = Organization(organization_name)
        self.organizations.append(new_organization)
        print(f"Organization '{organization_name}' added successfully.")
        return new_organization


if __name__ == "__main__":
    booking_system = ConferenceRoomBookingSystem()

    floor1 = ConferenceRoomBookingSystem.add_floor(1)
    floor1.rooms.append(Room("Room A", 10, True))
    floor1.rooms.append(Room("Room B", 8, False))
    floor1.rooms.append(Room("Room C", 12, True))

    floor2 = ConferenceRoomBookingSystem.add_floor(2)
    floor2.rooms.append(Room("Room D", 20, True))
    floor2.rooms.append(Room("Room E", 5, False))

    floor3 = ConferenceRoomBookingSystem.add_floor(3)
    floor3.rooms.append(Room("Room F", 40, True))

    org1 = booking_system.add_organization("Tech Inc 1")
    org2 = booking_system.add_organization("Tech Inc 2")

    admin_user1 = org1.add_admin_user(
        "Admin User", "admin@techinc1.com", "ADMIN")
    admin_user2 = org2.add_admin_user(
        "Admin User", "admin@techinc2.com", "ADMIN")

    normal_user1 = admin_user1.add_normal_user(
        "Normal User1", "normal@techinc1.com", "NORMAL")
    normal_user2 = admin_user2.add_normal_user(
        "Normal User2", "normal@techinc2.com", "NORMAL")

    print("User 1 viewing rooms by time")
    print()
    searched_rooms = normal_user1.view_rooms_by_time(
        "2023-09-16 10:00", "2023-09-16 11:00")
    print()

    print("User 1 books room")
    print()
    normal_user1.book_room(
        searched_rooms[0], "2023-09-16 10:00", "2023-09-16 12:00")

    print()
    print("User 1 viewing all rooms")
    print()
    normal_user1.view_all_rooms()

    print()
    print("User 1 books room for another time slot")
    print()
    normal_user1.book_room(
        searched_rooms[0], "2023-09-16 12:00", "2023-09-16 15:00")

    print()
    print("User 2 books room for prev time")
    print()
    normal_user2.book_room(
        searched_rooms[1], "2023-09-16 12:00", "2023-09-16 15:00")

    print()
    print("User 1 viewing all bookings")
    print()
    normal_user1.view_bookings()

    print()
    print("User 2 viewing all bookings")
    print()
    normal_user2.view_bookings()

    print()
    booking_id_to_cancel = next(
        iter(normal_user1.get_bookings().values())).booking_id
    print("User 1 cancels 1st booking", booking_id_to_cancel)
    print()

    normal_user1.cancel_bookings(booking_id_to_cancel)

    print()
    print("User 1 viewing booking")
    print()
    normal_user1.view_bookings()
