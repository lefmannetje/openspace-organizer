list_seats = [] # list of seats with user on it. Contains Seat class instances.
list_tables = [] # list of tables with seats on it. Contains Table class instances.

class Seat(object):
    def __init__(self):
        self.free = True
        self.occupant = ""
        self.list_seats = list_seats

    def set_occupant(self, name):
        self.free = False
        self.occupant = name

    def remove_occupant(self):
        self.free = True
        self.occupant = ""        

class Table(object):
    def __init__(self, seats) -> None:
        """     capacity which is an integer
                seats which is a list of Seat objects (size = capacity)  """
        self.capacity = 4           # how many seats can there be
        self.seats = seats          # how many seats are at the table

    def has_free_spot(self):
        #    has_free_spot() that returns a boolean (True if a spot is available)
        if len(self.seats) < self.capacity:
            return True
        else:
            return False

    def assign_seat(self, names):
        #    assign_seat(name) that places someone at the table
        for name in names:
            Seat = Seat()               # create seat instance
            Seat.set_occupant(name)     # give seat a person on it
            list_seats.append(Seat)     # fill list_seats[] with the seat object


    def left_capacity():
        #    left_capacity() that returns an integer
        pass
    
    def __str__(self) -> str:
        pass
        

#TODO add doctype for each functionm print(set_occupant.__doc__) AND print(remove_occupant.__doc__)