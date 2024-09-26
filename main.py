"""
import everything you need to launch the organizer
Load the colleagues from the csv file or list
Launch the organizer. Display the results
"""
'''
3. The script reads your input file, and organizes your colleagues to random seat assignments. 
The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

python
input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# Creates a list that contains all the colleagues names
names = utils.read_names_from_csv(input_filepath)

# create an OpenSpace()
open_space = OpenSpace()

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()

'''
#inmport csv to be able to open and read csv files
import csv
from Utils.openspace import Openspace
from Utils.table import Seat

#create filepath variables
input_filepath = "names.csv" 
output_filename = "output.csv"

#create empty list to fill up with participants
names = [] #list with names of participants

def create_names_list(): # Create a List form CSV with all names in it
    #open names.csv file as read
    with open(input_filepath, 'r') as file:
        #create csv_reader that contains all info
        csv_reader = csv.reader(file)
        #fill empty list row by row with each name being found.
        for row in csv_reader:
            names.append(row[0])

#how many tables do we need?
"""We are gonna calculate the number of tables based on the number of names"""
def number_of_tables(n):
    #we know each table has 4 seats so we divide the number of names by 4 to see how many teables we need
    number_of_tables = len(n) / 4
    print(number_of_tables)
    return number_of_tables

# 1) create name list
create_names_list() #OUTPUT: names[list]
print("We created our names LIST")

# 3) create tables

# 4) assign Seats until all tables are full

# create an OpenSpace()
open_space = Openspace(8, number_of_tables(names))
