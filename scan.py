# Scan.py
# @Author: Chris Dellinger
# @Version 5/13/2023
#
# This program is meant to be used by the Avery County School System in order
# to aid with the MacBook and iPad takeup process. When running the script,
# a USB barcode scanner can be used to scan the student ID barcodes located
# on the labels that are placed on all student devices. Current features
# include barcode scanner support, manual data entry support, an automatic
# backup feature, and a custom file name option.
#
# NOTES:
# Run this script by typing "python3 scan.py [output file name]
# If no output file name is specified, a default file name of "output.csv" will be created.

# coding: utf-8
import sys
import os
import csv
import shutil
from student_information import student_info

NUM_COLS = 10       # How many columns will be in output .csv file.
ID_INDEX = 0        # Index positions of the student info list.
LNAME_INDEX = 1
FNAME_INDEX = 2
SCHOOL_INDEX = 3
GRADE_INDEX = 4
HOMEROOM_INDEX = 5
CASE_INDEX = 6
CHARGER_INDEX = 7
COMPLETE_INDEX = 8
EMAIL_INDEX = 9
FILE_NAME = ""

# Display instructions on how to use this program.
def help():
    print()
    print('-' * 87)
    print('-- Scan a student device label barcode to begin the entry for that student.')
    print('-- Scan the case or charger master barcode or type "case" or "charger" to record the item as "missing".')
    print('-- Enter "c" to clear missing item data for current student.')
    print('-- Scan the next barcode to finalize the current entry and write it to a .csv file.')
    print('-- Enter "q" to quit the program. Data for current student will be saved.')
    print('-- Enter "h" to display the help menu.')
    print('-- Enter "s" to display a summary of the current student')
    print('-- Once the script finishes, a backup of the .csv file and a list of errors will be placed on your desktop.')
    print('-' * 87)
    print()

# Print an introductory summary about what the script is.
def intro():
    print()
    print('ACS Student Device Takeup Helper')
    print()
    print('This script is meant to be used by the Avery County School System in order')
    print('to aid with the MacBook and iPad takeup process. When running the script,')
    print('a USB barcode scanner can be used to scan the student ID barcodes located')
    print('on the labels that are placed on all student devices. Current features')
    print('include barcode scanner support, manual data entry support, an automatic')
    print('backup feature, and a custom file name option.')
    print()



# Print out a brief summary of each student's missing/received items.
# Info = [ID, LName, FName, School, Grade, Homeroom, Case, Charger, Complete, Email]
def show_info(info):
    print()
    print()
    print(f"Student ID: {info[0]}")
    print(f"Last Name:  {info[1]}")
    print(f"First Name: {info[2]}")
    print(f"School:     {info[3]}")
    print(f"Grade:      {info[4]}")
    print(f"Homeroom:   {info[5]}")
    print(f"Case        {info[6]}")
    print(f"Charger:    {info[7]}")
    status = ""
    if info[COMPLETE_INDEX] == "Complete":
        status = "All items received."
    else:
        status = "Student has missing items."
    print(status)
    print()

# Locate the current user's desktop folder so a backup can be created.
def get_user_desktop_path():
    user = [x for x in os.listdir('/Users/') if x not in ['.localized', 'Shared', 'mac',"Chris"]]

    desktop = '/Users/' + user[0] + '/Desktop/'
    return desktop

# Create a copy of the output file and error file and place it on the desktop.
def backup_to_desktop(user):
    directory = FILE_NAME[:-4]
    error_file = FILE_NAME[:-4] + '_errors.csv'
    file_path = user
    os.makedirs(os.path.join(user, directory), exist_ok=True)
    if error_file in os.listdir():
        shutil.copy(error_file, os.path.join(user, directory))
    shutil.copy(FILE_NAME, os.path.join(user, directory))
    print()
    print(FILE_NAME + ' has been backed up to your desktop at: ')
    print(file_path + directory)

# Reset the info list to the default values.
def reset_info(info):
    return [info[ID_INDEX],
            info[LNAME_INDEX],
            info[FNAME_INDEX],
            info[SCHOOL_INDEX],
            info[GRADE_INDEX],
            info[HOMEROOM_INDEX],
            'Received',
            'Received',
            '']

# Check to see if student ID is located in the list of all students.
def verify_student(student_id):
    if student_id in student_info:
        return True
    print('Student not found. Please scan another.')
    return False

# Create a csv file that contains a list of student IDs that were not found in the PowerSchool export.
def output_errors(file_name, error_list):
    error_file = file_name[:-4] + '_errors.csv'
    print('Saving list of errors to ' + error_file)
    if len(error_list) == 0:
        print('No errors were found.')
        return
    else:
        with open(error_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID'])
            for student in error_list:
                writer.writerow([student])

#---------------- Run the script ----------------#

# Display instructions for how to use the script
intro()
help()

# Get the user's Desktop folder path. This is where a backup of the data will be saved.
user = get_user_desktop_path()

# Determine what the output file should be saved as.
FILE_NAME = str(input('Enter the name of the .csv file that will be created: '))
if FILE_NAME == '':
    print('No file name entered. File will be save as "scanfile.csv"')
    FILE_NAME = 'scanfile.csv'
if not FILE_NAME.endswith('.csv'):
    FILE_NAME += '.csv'
else:
    FILE_NAME = 'output.csv'

print('\nBegin writing to file: ' + FILE_NAME)
print('\nStart by scanning a student ID barcode:')

# Create a list containing student numbers that were not found in the master student list.
errors = []

# Open the .csv file for writing and specify the column names.
with open(FILE_NAME, 'w', newline='') as file:
    info = [''] * NUM_COLS
    writer = csv.writer(file)
    writer.writerow(['Student ID','LName','FName', 'School','Grade', 'Homeroom', 'Case', 'Charger', 'Complete', 'Email'])

# Run the main loop of the program. Read in student ID barcodes and
# missing items and write to the output file. Student names, grade levels, and
# homeroom are retrieved from the supplemental "student_information" file.
    while True:
        scan = str(input())
        if scan == 'q':
            if info[CASE_INDEX] == info[CHARGER_INDEX] == "Received":
                info[COMPLETE_INDEX] = 'Complete'
            writer.writerow(info)
            break
        if scan == 'h':
                help()
        if scan.isdigit():
            if verify_student(scan):
                if info[ID_INDEX] != '':
                    if info[CASE_INDEX] == info[CHARGER_INDEX] == "Received":
                        info[COMPLETE_INDEX] = "Complete"
                    show_info(info)
                    writer.writerow(info)
                student = student_info[scan]
                lname = student['lname']
                fname = student['fname']
                school = student['school']
                grade = student['grade']
                homeroom = student['homeroom']
                email = scan + '@averyschools.net'
                info = [scan, lname, fname, school, grade, homeroom, 'Received', 'Received','', email]
                print('Scan or type the missing items:')
            else:
                errors.append(scan)
                print('Student number will be written to "' + FILE_NAME[:-4] + '_errors.csv"')
        else:
            if scan.lower() == 'case':
                info[CASE_INDEX] = 'Missing'
            elif scan.lower() == 'charger':
                info[CHARGER_INDEX] = 'Missing'
            elif scan.lower() == 'c':
                print('Current student info cleared. Enter missing items:')
                info = reset_info(info)
            elif scan.lower() == 's':
                show_info(info)

# Create a backup of the .csv file and error log on the current user's desktop.
output_errors(FILE_NAME, errors)
backup_to_desktop(user)
