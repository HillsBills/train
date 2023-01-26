import employees_class
import attendance_class
import re
import csv
import datetime

address_e = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv'
address_a = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv'
employee = employees_class.Employees(address_e)
attend = attendance_class.Attendance(address_a)


# TODO Its ok for main to have functions. If there are many they can move to a special class.
#  If these functions arent connected directly to the classes there isnt a reason for them to be in the class.


def check_str(inp, func, opposite):
    '''
    checks the type of the input and returns the input
    :param inp: str
    :param func: function
    :param opposite: str
    :return: input
    '''
    while not func(opposite):
        opposite = input(f'Enter {inp} ')
    return opposite


#
def check_date():
    """
    Validates input entered is digits.
    Tries to create a date object from the input.
    :return: date
    """
    while True:
        year = int(check_str('year', str.isdigit, 'i'))
        month = int(check_str('month', str.isdigit, 'i'))
        day = int(check_str('day', str.isdigit, 'i'))
        try:
            date = datetime.datetime(year, month, day)
            if date <= datetime.datetime.now():
                return date
        except ValueError as w:
            print(w)
        except TypeError as w:
            print(w)


#
def check_address(func, fields):
    """
    checks the file exists.
    creates a reader for the file and checks if its empty. file can have headers or not.
    runs the function
    :param func: function
    :param fields: list
    :return: print or function
    """
    while True:
        file = input('Enter file address ')
        file = re.sub(r'\\', r'\\\\', file)
        try:
            with open(file) as f:
                line = f.readline()
                f.seek(0)
                #
                if line == f"{','.join(fields)}\n":
                    fields = None

                reader = list(csv.DictReader(f, fields, restval=''))
                if not reader:
                    return print('Empty file')
                return func(reader)

        except FileNotFoundError as w:
            print(w)
        except OSError as w:
            print(w)


# def check_address(func):
#     '''
#     checks the file exists and runs the function
#     :param func: function
#     '''
#     while True:
#         file = input('Enter file address ')
#         file = re.sub(r'\\', r'\\\\', file)
#         try:
#             with open(file) as f:
#                 func(f)
#         except FileNotFoundError as w:
#             print(w)
#         except OSError as w:
#             print(w)


# TODO if i have utilites( helper functions) which i use in several pages, i may think of having a class of utilities.
# TODO( should i make a check class? with all the checks will be in functions?
# in any case all checks (unless the check is small or the function is small) need to be in separate functions.
#  otherwise the original functions will be too long)
# TODO add exceptions etc. (functions that i can duplicate? add the validation functions in the class, outside the functions)
# the checks should be in main. in whiles and no except if not working with a file,
# or not working with something that will crash otherwise. except can be in the class.
# the parameter of the while can be a function if its a thing that repeats.

# make sure user didnt enter commas and shout as well (cause commas have a meaning in csv).
# maybe csv module can handle this

# TODO uncaps everything before putting as a parameter. (or maybe caps everything?) both input here and function.
while True:
    function = input(
        '\nFor ENDING the program type 0.\n\nFor ADDING an employee manually type 1.\nFor ADDING from a FILE type 2.\n'
        'For DELETING an employee manually type 3.\nFor DELETING employees from a FILE type 4.\n'
        'For SEARCHING an employee type 5.\nFor marking your ATTENDANCE type 6.\n'
        'For generating an EMPLOYEE report type 7.\nFor generating current MONTH\'S attendance report type 8.\n'
        'For generating LATE attendance report type 9. \nFor a DATE RANGE attendance report type 10. \n')
    if function == '0':
        break
    elif function == '1':
        employee_id = check_str('employee_id', str.isdigit, 'i')
        name = (check_str('name', str.isalpha, '1')).title()
        phone = check_str('phone', str.isdigit, 'i')
        age = check_str('age', str.isdigit, 'i')
        level = (check_str('level if applicable: senior manager, manager, senior or junior',
                           lambda level: level in employees_class.Employees.levels, 'i')).title()
        # - what level would you like? save answer in set. would you like more? continue. or break. until 3 runs.
        #  and then run the function with the set
        # if not level:
        #     level = None
        #     print('none')
        employee.add_employee(employee_id, name, phone, age, level)

    elif function == '2':
        check_address(employee.add_employees_from_file, employees_class.Employees.fieldnames)

    elif function == '3':
        employee_id = check_str('employee_id', str.isdigit, 'i')
        employee.delete_employee(employee_id)

    elif function == '4':
        check_address(employee.delete_employees_from_file, ['employee_id'])
    #
    elif function == '5':
        param = (check_str('employee', str.isalnum, '*')).title()
        # additional = False
        # if input('If you would like employee information, type y. otherwise press ENTER '):
        #     additional = True
        #
        additional = employee.search_employee([param], additional=True)
        if not additional:
            print(employees_class.Employees.not_exist)
        else:
            # print(f'Employee ID {ID}, {name}, ', additional)
            print(additional)

    elif function == '6':
        employee_id = check_str('employee_id', str.isdigit, 'i')
        attend.mark_attendance(employee_id, employee)

    elif function == '7':
        employee_id = check_str('employee_id', str.isdigit, 'i')
        attend.employee_attendance_report(employee_id)

    elif function == '8':
        attend.current_month_attendance_report()

    elif function == '9':
        attend.late_attendance_report()
    #
    elif function == '10':
        # TODO make sure higher than 2021. make sure month. make sure day.
        #  make sure until is not lower date.
        #  make sure dates are not later than today
        print('Enter From date')
        _from = check_date()
        print('Enter Until date')
        until = check_date()
        if until < _from:
            until, _from = _from, until
        # until = datetime.datetime(1, 1, 1)
        # while until < _from:
        #     # print('until can not be earlier than from')
        #     print('Enter Until date')
        #     until = check_date()
        attend.date_range_attendance_report(until, _from)
        # _from = datetime.datetime(2021, 1, 7)
        # until = datetime.datetime(2021, 1, 17)
    else:
        continue
    # break
