# vehicle management system for a rental company
# vehicles have names, seats and availability

class Vehicle:

    def __init__(self, name, seats):
        self._name = name
        self._seats = seats
        self._renter = ""
        self._available = True
        vehicles.append(self)

    def _hire(self, renter):
        self._available = False
        self._renter = renter

    def _return(self):
        self._available = True
        self._renter = ""

# vehicles list to store all objects
vehicles = []

# create vehicles
Vehicle("Subaru Outback", 5)
Vehicle("Ford Escape", 5)
Vehicle("Toyota Hiace", 8)

# display all vehicles
def view_all():
    for v in vehicles:
        print("{}, ({})".format(v._name, v._seats))

# display available based on seats
def available():
    pass

view_all()

