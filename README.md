A Collection of scripts and programs that I have created during my time working at Avery County Schools.

These programs are as follows:

## Random Pair.py
A program that generates randomly chosen pairs of letters and numbers without replacement. Used for classroom seating assignments.

## add_colons.py
Function to add colons to a mac address string.

User should input the string they want to be separated by colons
and the sctipt will return the colon-separated mac address

This function was used when formatting a large number of exported
mac addresses that did not include the colon separators.

Example: A1B2C3D4E5F6G7H8 Formats to A1:B2:C3:D4:E5:F6:G7:H8

## bintodec.py
A simple script that converts a binary number into its decimal form

## csv_to_dict.py
This function takes a csv file of exported student data and
formats and inserts the data into a python dictionary to
speed up the lookups.

This function was used in conjunction with scan.py in order to
inventory student devices and keep track of any missing items
students might be missing.

## scan.py - A command line inventory management system
This program is meant to be used by the Avery County School System in order
to aid with the student MacBook and iPad takeup process. When running the script,
a USB barcode scanner can be used to scan the student ID barcodes located
on the labels that are placed on all student devices. Current features
include barcode scanner support, manual data entry support, an automatic
backup feature, and a custom file name option.

## dice.py
A fun program used to simulate dice rolls and optionally display hte results as ASCII characters.

## nato.py
A script used to translate a string of letters into a string of NATO alphabet terms. 

Example: ABC --> "Alpha Bravo Charlie"

## search_for_app.sh
This script prompts the user for the title of an app and then searches the 
device to see if the app is installed

This script was originally designed to be executed remotely on student devices to 
periodically scan for any unapproved or dangerous apps. If you wish to send it remotely,
uncomment the "APPNAME = "VLC" line and replace the string with whichever app you wish
to search for. Then comment out the echo and read lines below it.

By default, this script is designed to email the results of the scan to the users listed below.
If extra users are to be added, simply add their emails to the end of the "mail" command, 
separated by spaces if there are multiple addresses.

## shuffle.py
A simple function to shuffle the contents of an array

## split_data.py
This program uses pandas to split a master file of data into multiple files based
on the unique values in a given column.

After running this function, the user will be asked to enter the name of the source csv file
and the column they want to split up. The function will then create a separate file for each
unique value in the specified column. Each file will contain all records for each unique
column header in the source file.

Example: A data file contains student data and has a column indicating which school the student attends.
By running this function and entering the "school" column name, the csv file will be split into multiple csv files, one for each school.

## split_list.py
Function to split a large list of items into multiple evenly sized lists.
If the number cannot be evenly split into equal length lists, then the remainder
will be added into a list that contains all remaining items that are left over

@param items: The list of items the user wishes to split up
@param num_per_list: The number of items per list

Example: if the user has a list of 750 items and specifies that each new list should contain 100 items, this function
will return a list of lists, with 7 lists of length 100 and one list of length 50.

