from .table import Table, Seat
class Openspace():
    def __init__(self, list_tables, number_of_tables, list_seats) -> None:
        """
        tables which is a list of Table. (you will need to import Table from table.py).
        number_of_tables which is an integer.
        """
        self.list_tables = list_tables              # contains all the Table instances [LIST]
        self.list_seats = list_seats              # contains all the Seats instances [LIST]
        self.number_of_tables = number_of_tables    # int of how many tables there will be in the open sapce ==> in this case 6
        
    def organize(self, names):      
        #randomly assign people to Seat objects in the different Table objects.

        for name in names: # for each name in the list we wanna assign the chair to a table and put a person on it
            for table in self.list_tables:
                #assign someone to a chair if it's empty
                #table.assign_seat(name)
                # if table.has_free_spot():
                table.assign_seat(name, self.list_seats)


    def display():
        #display the different tables and there occupants in a nice and readable way
        pass

    def store():
        #store the repartition in an excel file
        pass

    def __str__(self):
        return self.number_of_tables, self.list_tables

#TODO str + docfile
