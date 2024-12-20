class Hotel:
    def __init__(self):
        self.rooms = {101: None, 102: None, 103: None, 104: None, 105: None}
    
    def view_rooms(self):
        print("\nAvailable Rooms:")
        for room, guest in self.rooms.items():
            status = "Available" if guest is None else f"Booked by {guest['name']}"
            print(f"Room {room}: {status}")
    
    def book_room(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        available_rooms = [room for room, guest in self.rooms.items() if guest is None]
        
        if not available_rooms:
            print("\nSorry, no rooms are available.")
            return
        
        print(f"\nAvailable Rooms: {', '.join(map(str, available_rooms))}")
        try:
            room_number = int(input("Enter room number to book: "))
            if room_number in available_rooms:
                self.rooms[room_number] = {"name": name, "phone": phone}
                print(f"Room {room_number} has been booked successfully!")
            else:
                print("Invalid room number or room is already booked.")
        except ValueError:
            print("Invalid input. Please enter a valid room number.")
    
    def cancel_booking(self):
        try:
            room_number = int(input("Enter room number to cancel booking: "))
            if room_number in self.rooms and self.rooms[room_number] is not None:
                print(f"Booking for Room {room_number} has been canceled.")
                self.rooms[room_number] = None
            else:
                print("Invalid room number or no booking found.")
        except ValueError:
            print("Invalid input. Please enter a valid room number.")
    
    def view_customers(self):
        print("\nCustomer Details:")
        customers_found = False
        for room, guest in self.rooms.items():
            if guest:
                customers_found = True
                print(f"Room {room}: {guest['name']} (Phone: {guest['phone']})")
        if not customers_found:
            print("No customers found.")
    
    def menu(self):
        while True:
            print("\n--- Hotel Booking System ---")
            print("1. View available rooms")
            print("2. Book a room")
            print("3. Cancel booking")
            print("4. View customer details")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.view_rooms()
            elif choice == "2":
                self.book_room()
            elif choice == "3":
                self.cancel_booking()
            elif choice == "4":
                self.view_customers()
            elif choice == "5":
                print("Thank you for using the Hotel Booking System!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of Hotel and call the menu
hotel = Hotel()
hotel.menu()
