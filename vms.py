# vehicle management system for a rental company
# vehicles have names, seats availability and renters
# testing commit comments

class Vehicle:

    def __init__(self, name, seats, licence):
        self._name = name
        self._seats = seats
        self._licence = licence
        self._renter = ""
        self._available = True
        vehicles.append(self)

    def _display_info_available(self):
        print("============")
        print(self._name)
        print("Seats: {}".format(self._seats))
        print("Licence: {}".format(self._licence))

    def _display_all(self):
        print("===============")
        print(self._name)
        print("Seats: {}".format(self._seats))
        print("Licence: {}".format(self._licence))
        if self._available == True:
            print("Available")
        else:
            print("Currently unavailable. Renter name: {}".format(self._renter))

    def _hire(self, renter):
        self._available = False
        self._renter = renter

    def _return(self):
        self._available = True
        self._renter = ""

# vehicles list to store all objects
vehicles = []

# create vehicles
Vehicle("Subaru Outback", 5, "ABC123")
Vehicle("Ford Escape", 5, "TYG321")
Vehicle("Toyota Hiace", 8, "AAB3")



# display available based on seats
def rent_vehicle():
    print("Enter number of seats required:")
    while True:
        try:
            seat_search = int(input("Seats: "))
            break
        except:
            print("Enter an integer")
    for v in vehicles:
        if v._seats >= seat_search and v._available ==True:
            v._display_info_available()
    
    rent_out = input("Enter number of vehicle to rent: ")
    renter_name = input("Enter renter name:")
    counter = 0
    for v in vehicles:
        if v._licence == rent_out:
            v._hire(renter_name)
            counter +=1
    if counter == 0:
        print("Licence plate incorrect. No vehicle rented")
    main_menu()

def return_vehicle():
    return_name = input("Enter your name:") 
    for v in vehicles:
        if v._renter == return_name:
            v._display_info_available()
    return_licence = input("Enter licence number:")
    for v in vehicles:
        if v._renter == return_name and v._licence == return_licence:
            v._return()
    main_menu()

def main_menu():
    print("Vehicle management system")
    print("-------------------------")
    print("1. View all vehicles")
    print("2. Rent vehicle")
    print("3. Return vehicle")
    while True:
        try:
            selection = int(input("Choice:"))
            if selection in range(1, 4):
                break
            else:
                print("Enter valid number")
        except:
            print("Enter an integer")
    if selection==1:
        for v in vehicles:
            v._display_all()
        main_menu()
    elif selection==2:
        rent_vehicle()
    else:
        return_vehicle()

main_menu()
