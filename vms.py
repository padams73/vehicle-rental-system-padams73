# vehicle management system for a rental company
# vehicles have names, seats and availability

class Vehicle:

    def __init__(self, name, seats):
        self._name = name
        self._seats = seats
        self._available = True
        vehicles.append(self)

    def _display_info(self):
        print("Vehicle: {} ({})".format(self._name, self._seats))


    def _hire(self):
        self._available = False

    def _return(self):
        self._available = True

# vehicles list to store all objects
vehicles = []

# create vehicles
Vehicle("Subaru Outback", 5)
Vehicle("Ford Escape", 5)
Vehicle("Toyota Hiace", 8)

# display all vehicles
def view_all():
    for v in vehicles:
        v._display_info()

# display available based on seats
def available():
    pass