import uuid


class Booking:
    def __init__(self, user, room, start_time, end_time, organization):
        self.booking_id = str(uuid.uuid4())  # Generate a unique booking ID
        self.user = user
        self.room = room
        self.start_time = start_time
        self.end_time = end_time
        self.organization = organization

    def get_booking_id(self):
        return self.booking_id

    def get_user(self):
        return self.user

    def get_room(self):
        return self.room

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_organization(self):
        return self.organization

    # Additional methods can be added for managing and modifying bookings if needed.
