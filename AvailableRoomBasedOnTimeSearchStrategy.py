from datetime import datetime
from SearchStrategy import SearchStrategy


class AvailableRoomBasedOnTimeSearchStrategy(SearchStrategy):
    def __init__(self, start_time, end_time):
        self.date_format = "%Y-%m-%d %H:%M"  # Define the date format
        try:
            self.start_time = datetime.strptime(start_time, self.date_format)
            self.end_time = datetime.strptime(end_time, self.date_format)
        except ValueError as e:
            print("Error parsing dates:", e)

    def search(self, rooms):
        results = []
        for room in rooms:
            found_flag = False
            for booking in room.get_bookings():
                try:
                    booking_start = datetime.strptime(
                        booking.get_start_time(), self.date_format)
                    booking_end = datetime.strptime(
                        booking.get_end_time(), self.date_format)

                    if not (booking_start > self.start_time and self.start_time > booking_end) and not (booking_start > self.end_time and self.end_time > booking_end):
                        found_flag = True
                except ValueError as e:
                    print("Error parsing dates:", e)

            if not found_flag:
                results.append(room)
        return results
