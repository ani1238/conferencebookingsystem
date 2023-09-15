from RoomSearchManager import RoomSearchManager
from datetime import datetime


class Room:
    def __init__(self, roomName, capacity, hasProjector):
        self.roomName = roomName
        self.capacity = capacity
        self.isAvailable = True  # Initialize as available
        self.floor = None  # Reference to the floor where the room is located
        self.bookings = []
        self.hasProjector = hasProjector
        RoomSearchManager.add_room_to_tree(self)

    def get_room_name(self):
        return self.roomName

    def get_capacity(self):
        return self.capacity

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_bookings(self):
        return self.bookings

    def is_available(self, start_time, end_time):
        date_format = "%Y-%m-%d %H:%M"

        try:
            start = datetime.strptime(start_time, date_format)
            end = datetime.strptime(end_time, date_format)

            for booking in self.bookings:
                booking_start = datetime.strptime(
                    booking.get_start_time(), date_format)
                booking_end = datetime.strptime(
                    booking.get_end_time(), date_format)

                # Check for overlap between the requested time slot and existing bookings
                if start < booking_end and end > booking_start:
                    return False  # Room is already booked during this time

            # No overlap with existing bookings, so the room is available
            return True
        except ValueError:
            # Handle date parsing errors if necessary
            print("Error parsing dates")
            return False  # Consider it unavailable due to parsing error

    def set_availability(self, available):
        self.isAvailable = available

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def has_projector(self):
        return self.hasProjector
