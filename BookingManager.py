from Room import Room
from RoomSearchManager import RoomSearchManager
from datetime import datetime
from collections import OrderedDict
from Booking import Booking


class BookingManager:
    def __init__(self):
        self.bookings = OrderedDict()

    def book_room(self, user, room, start_time, end_time):
        date_format = "%Y-%m-%d %H:%M"

        try:
            start = datetime.strptime(start_time, date_format)
            end = datetime.strptime(end_time, date_format)
            hours = (end - start).total_seconds() / 3600

            if user.get_organization().get_total_time() + hours > 30:
                print("Time limit exceeded of 30 hours")
                return False

            if room.is_available(start_time, end_time):
                print("Room is being booked " + room.get_room_name())
                booking = Booking(user, room, start_time,
                                  end_time, user.get_organization())
                self.bookings[booking.get_booking_id()] = booking
                self.list_bookings()
                room.add_booking(booking)
                room.set_availability(False)
                user.get_organization().set_total_time(
                    user.get_organization().get_total_time() + hours)
                return True
        except ValueError as e:
            print("Error parsing dates:", e)

        return False

    def cancel_bookings(self, user, booking_id):
        date_format = "%Y-%m-%d %H:%M"

        try:
            now = datetime.now()
            booking_start = datetime.strptime(
                self.bookings[booking_id].get_start_time(), date_format)
            diff = (booking_start - now).total_seconds() / 60

            if diff > 15:
                del self.bookings[booking_id]
                user.get_organization().set_total_time(
                    user.get_organization().get_total_time() - 0.25)
                print("Booking with ID " + booking_id + " is canceled")
                return True
            else:
                print(
                    "You should cancel the conference before 15 mins of start time. Unable to cancel conference now")
                return False
        except (ValueError, KeyError) as e:
            print("Error:", e)
            return False

    def list_bookings(self, user=None):
        if user:
            for booking_id, booking in self.bookings.items():
                if booking.get_user() == user:
                    print("Booking ID:", booking_id)
                    print("User:", booking.get_user().get_name())
                    print("Room:", booking.get_room().get_room_name())
                    print("Start Time:", booking.get_start_time())
                    print("End Time:", booking.get_end_time())
                    print()
        else:
            for booking_id, booking in self.bookings.items():
                print("Booking ID:", booking_id)
                print("User:", booking.get_user().get_name())
                print("Room:", booking.get_room().get_room_name())
                print("Start Time:", booking.get_start_time())
                print("End Time:", booking.get_end_time())
                print()

    def get_bookings_by_user(self, user):
        bookings_by_user = OrderedDict()
        for booking_id, booking in self.bookings.items():
            if booking.get_user() == user:
                bookings_by_user[booking_id] = booking
        return bookings_by_user

    def search_rooms(self, search_strategy):
        search_results = RoomSearchManager.get_room_search_tree().search_rooms(search_strategy)
        found_flag = False
        for room in search_results:
            found_flag = True
            print("Room:", room.get_room_name() +
                  ", Capacity:", room.get_capacity())
        if not found_flag:
            print("Room with such criteria does not exist")
        return search_results
