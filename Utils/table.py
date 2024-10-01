class Seat(object):
    def __init__(self):
        self.free = True                # Boolean if True seat is empty
        self.occupant = ""              # String with occupants name

    def set_occupant(self, name):
        if self.free: 
            self.free = False
            self.occupant = name

    def remove_occupant(self): 
        self.free = True
        self.occupant = ""        
    
    def __str__(self):
        return f'{self.free},{self.occupant},{self.list_seats}'

class Table(object):
    _counter = 0

    def __init__(self):
        """     capacity which is an integer
                seats which is a list of Seat objects (size = capacity)  """
        self.capacity = 4                       # how many seats can there be
        self.seats = []                         # how many seats are at the table. only 4 seats
        Table._counter +=1                      # keeps track of how many instances are created
        self.name = f"Table_{Table._counter}"   # give each instance a recognizable name

    def has_free_spot(self):
        #    has_free_spot() that returns a boolean (True if a spot is available)
        if len(self.seats) < self.capacity:
            return True
        else:
            return False

    def assign_seat(self, list_seats):
        # assign_seat(name) that places someone at the table
        # assign name to the first free seat
        for seat in list_seats:
            print(name)
            #seat.set_occupant(name)

    def left_capacity():
        #    left_capacity() that returns an integer
        pass


    def __str__(self):
        occupied_seats = [str(seat) for seat in self.seats if seat.occupant is not None]
        return f"Table(name={self.name}, capacity={self.capacity}, seats={occupied_seats})"
        

#TODO add doctype for each functionm print(set_occupant.__doc__) AND print(remove_occupant.__doc__)