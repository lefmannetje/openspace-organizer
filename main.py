#inmport csv to be able to open and read csv files
import csv
import random
from Utils.openspace import Openspace
from Utils.table import Seat, Table

#create filepath variables
input_filepath = "names.csv" 
output_filename = "output.csv"

#create empty lists
list_seats = []     # list of seats with user on it. Contains Seat class instances.
list_tables = []    # list of tables with seats on it. Contains Table class instances.
list_names = []     # list with names of participants

def create_list_names(): # Create a List form CSV with all names in it
    #open names.csv file as read
    with open(input_filepath, 'r') as file:
        #create csv_reader that contains all info
        csv_reader = csv.reader(file)
        #fill empty list row by row with each name being found.
        for row in csv_reader:
            list_names.append(row[0])

#how many tables do we need?
"""We are gonna calculate the number of tables based on the number of names"""
def number_of_tables(n):
    #we know each table has 4 seats so we divide the number of names by 4 to see how many teables we need
    number_of_tables = len(n) / 4
    print(number_of_tables)
    return number_of_tables

# 1) create name list and randomize it with the shuffle command
create_list_names() #OUTPUT: names[list]
random.shuffle(list_names)
print(" ==-- list_names created and Randomized --==")

# 2) create seats
n_seats = int(len(list_names))

for i in range(0 , n_seats):    # we make n seats depending on how many names there are in list.
    seat_item = Seat()
    list_seats.append(seat_item)
print("==-- list_seats created --==")

# 3) create tables
n_tables = int(len(list_names) / 4)     # calculate how many tables we minimum need : 6

for i in range(0 , n_tables):           # we make n seats depending on how many names there are in list.
    table_item = Table()
    list_tables.append(table_item)
print(" ==-- list_tables created --==")

# 4) Create openspace
openspace_item = Openspace(list_tables, n_tables, list_seats)
print(" ==-- Openspace created --==")
#this will have now 4 empty TABLE instances

# 5) Assign a colleague randomly to a table
"""We want to assign each person from the list to a table. We gonna fill a table untill it's full and than move to the next on."""
openspace_item.organize(list_names)
 
# save the seat assigments to a new file
# open_space.store(output_filename)

# display assignments in the terminal
openspace_item.display()