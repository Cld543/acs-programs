# coding: utf-8
'''
Script used at Avery County Schools.

This function takes a csv file of exported student data and
and formats and inserts the data into a python dictionary to
speed up the lookups.

This function was used in conjunction with scan.py in order to
inventory student devices and keep track of any missing items
students might be missing.
'''
def csv_to_dict(csv_file):
    student_info = {}
    row_count = 0
    with open(csv_file, 'r') as fp:
        for row in fp:
            if row_count != 0:
                info = row.split(',')
                student_id = info[0]
                lname = info[1]
                fname = info[2]
                school = info[3]
                grade = info[4]
                homeroom = info[5]#[:-1]
                student_info[student_id] = {}
                student_info[student_id]['lname'] = lname
                student_info[student_id]['fname'] = fname
                student_info[student_id]['school'] = school
                student_info[student_id]['grade'] = grade
                student_info[student_id]['homeroom'] = homeroom
            row_count += 1
    print(f"Converted {row_count} entries of student data into dictionary format.")
    return student_info
    
