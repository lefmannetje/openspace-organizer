class Seat(object):
    def __init__(self, free, occupant) -> None:
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        """
        Class that will perform the init operation when getting created.
        :param free: A BOOLEAN that will be added to the second parameter.
        :param occupant: A STRING that will be added to the fist parameter.
        """
        #    set_occupant(name) which allows the program to assign someone a seat if it's free
        pass

    def remove_occupant():
        """
        Class that will perform the init operation when getting created.
        :param free: A BOOLEAN that will be added to the second parameter.
        :param occupant: A STRING that will be added to the fist parameter.
        """
        #    remove_occupant() which remove someone from a seat and return the name of the person occupying the seat before
        pass

    def __str__(self) -> str:
        pass

class Table(object):
    def __init__(self, capacity, seats) -> None:
        """
        capacity which is an integer
        seats which is a list of Seat objects (size = capacity)
        """
        self.capacity = capacity
        self.seats = seats
        pass

    def has_free_spot():
        #    has_free_spot() that returns a boolean (True if a spot is available)
        pass

    def assign_seat(name):
        #    assign_seat(name) that places someone at the table
        pass

    def left_capacity():
        #    left_capacity() that returns an integer
        pass
    
    def __str__(self) -> str:
        pass
        

#TODO add doctype for each functionm print(set_occupant.__doc__) AND print(remove_occupant.__doc__)