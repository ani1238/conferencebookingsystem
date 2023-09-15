# conferencebookingsystem
ConferenceRoomBookingSystem written in Python 

You can run the code using the main function, there is no command line integrations as of now.

The code utilizes a B-Tree data structure to efficiently store and search for rooms based on various criteria, such as capacity, equipment, and booking slots.

The Strategy Design Pattern is employed to enable flexible room searches with different criteria. This pattern allows for easy expansion of search capabilities in the future.

The Composite Design Pattern is used to combine multiple search strategies, offering a comprehensive approach to room searches when needed.

The Observer Design Pattern is implemented to notify users belonging to an organization when their booking limit approaches 30 hours while they are using the application.

Booking cancellations are supported, with a restriction in place to prevent cancellations within 15 minutes of the booking's start time.

A locking mechanism akin to the one used in services like BookMyShow ensures that multiple users cannot book the same room simultaneously.

These design patterns and features enhance the functionality and usability of the application, making it a versatile and user-friendly conference room booking system.

