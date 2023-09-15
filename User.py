from datetime import datetime

from AvailableRoomBasedOnTimeSearchStrategy import AvailableRoomBasedOnTimeSearchStrategy
from Booking import Booking
from BookingManager import BookingManager
from CompositeSearchStrategy import CompositeSearchStrategy


class User:
    def __init__(self, name, email, role, organization):
        self.name = name
        self.email = email
        self.role = role
        self.organization = organization
        self.isAdmin = role == "ADMIN"
        self.bookings = {}
        self.bookingManager = BookingManager()

    def is_admin(self):
        return self.isAdmin

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_role(self):
        return self.role

    def get_organization(self):
        return self.organization

    def set_organization(self, organization):
        self.organization = organization

    def get_bookings(self):
        return self.bookingManager.get_bookings_by_user(self)

    def add_normal_user(self, name, email, role):
        user = self.organization.add_normal_user(self, name, email, role)
        return user

    def view_rooms_by_time(self, start_time, end_time):
        booking_search = AvailableRoomBasedOnTimeSearchStrategy(
            start_time, end_time)
        searched_rooms = self.bookingManager.search_rooms(booking_search)
        return searched_rooms

    def view_all_rooms(self):
        booking_search = CompositeSearchStrategy()
        searched_rooms = self.bookingManager.search_rooms(booking_search)
        return searched_rooms

    def book_room(self, room, start_time, end_time):
        success = self.bookingManager.book_room(
            self, room, start_time, end_time)

        if success:
            booking = Booking(self, room, start_time,
                              end_time, self.organization)
            self.bookings[booking.get_booking_id()] = booking
            print("Room booked successfully", room.get_room_name())
        return success

    def view_bookings(self):
        self.bookingManager.list_bookings(self)

    def cancel_bookings(self, booking_id):
        self.bookingManager.cancel_bookings(self, booking_id)
