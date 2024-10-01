import time
import csv
class Openspace():
    def __init__(self, list_tables, number_of_tables, list_seats) -> None:
        """
        tables which is a list of Table. (you will need to import Table from table.py).
        number_of_tables which is an integer.
        """
        self.list_tables = list_tables              # contains all the Table instances [LIST]
        self.list_seats = list_seats              # contains all the Seats instances [LIST]
        self.number_of_tables = number_of_tables    # int of how many tables there will be in the open sapce ==> in this case 6
        
    def organize(self, list_names):      
        #randomly assign people to Seat objects in the different Table objects.

        for i, name in enumerate(list_names): # Fill seats with people and assign them to tables
            #place person on empty seat
            self.list_seats[i].set_occupant(name)

            # check if table has open spot, if so put chair on it 
            if self.list_tables[i // 4].has_free_spot():
                self.list_tables[i // 4].seats.append(self.list_seats[i])
            else:
                print("Table is full, plz go to next table.")

    def display(self):
        print("This is the current table arangement!")
        #display the different tables and there occupants in a nice and readable way
        for i, table in enumerate(self.list_tables):
            print(f"=== {table.name} ===")
            for seat in table.seats:
                 print(seat.occupant)

    def store(self):
        # Define the headers
        headers = ['Table', 'user1', 'user2', 'user3', 'user4']
        data = []
        # Specify the file name
        timestr = time.strftime("%dY%m%Y-%H%M%S")
        filename = f'output.csv_{timestr}'

        # Write the headers to the CSV file
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

        print(f"CSV file '{filename}' has been created with the specified headers.")


    def __str__(self):
        return self.number_of_tables, self.list_tables

#TODO str + docfile
