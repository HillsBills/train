import employees
import attendance
# import re
import csv
import datetime

# TODO Its ok for main to have functions. If there are many they can move to a special class.
#  If these functions arent connected directly to the classes there isnt a reason for them to be in the class.

combination = []
header = []
combine = '\nWould you like to combine up to three reports? press y. \nIs this the last report? press e. \n' \
          'Otherwise press Enter. \n'
comb = ''
fields = employees.FIELDNAMES

def combining(func, *params):
    comb = input(combine)
    report = func(params, comb)
    if comb:
        report, title = report
        prepare_reports(report, comb, title)
    return comb


# todo- tidy funcs.
#  new
def prepare_reports(report, end, header1, header2=''):
    """
    creates the header and the list of reports before running the combination report function
    @param report: list
    @param end: str
    @param header1: str
    @param header2: str
    """
    header.append(header1)
    # header.extend([header1, header2])
    combination.append(report)
    if end == 'e':
        attendance.combination_attendance_report(combination, header)


#         todo- what if i try to update id?
def check_field(field):
    if field == fields[1]:
        # todo anna- why doesnt this work? whats a better way to check letters and spaces?
        # return str.replace(' ', '').isalpha
        # return lambda char, string: all(char.isalpha() or char.isspace() for char in string)
        return employees.is_name
    elif field == fields[4]:
        return employees.is_level
        # return lambda lev: lev in employees.LEVELS
    return str.isdecimal


# todo anna- which is better? mine or ofir
def o_validate_input(msg, valid_func):
    _input = input(f'Enter {msg}')
    while not valid_func(_input):
        _input = input(f'Enter {msg}')
    return _input.title()


def ois_valid_name(name):
    if all(x.isalpha() or x.isspace() for x in name) and len(name) >= 2:
        return True
    return False


def ois_valid_age(age):
    if age.isdecimal() and 14 < int(age) < 120:
        return True
    return False

#todo i can ask for title() here
oname = o_validate_input('Name', 'is_valid_name')
ophone = o_validate_input('Phone Number', 'is_valid_phone')
oage = o_validate_input('Age', 'is_valid_age')
olevel = o_validate_input('Level if applicable: senior manager, manager, senior or junior', 'is_valid_level')


# todo ofir- he suggests having a separate helper function for each input, that will check more than type.
#  like legel age, legal phone characters, legal date (will be another sort of check in the main function). legal id.
#  its more professional if i check legality of inputs. and then i will use these functions also in employee
#  to check data in files. a recursive function that will call itself when requierments arent met. instead of while not
#  or have a separate function for each validation, to save all the ifs in the big function.
#  the input loop can be a function

# string = input("Enter a string: ")
#
# if all(x.isalpha() or x.isspace() for x in string):
#     print("Only alphabetical letters and spaces: yes")
# else:
#     print("Only alphabetical letters and spaces: no")

# todo although levels are written as lower case, i always change them to capital before entering the file.
#  but i cant have only fields written as capitals. needs to be both or neither.
#  two options- either i change field in prepare file for title, or i remove the extra titles for level.
#  if removing the extra titles is good, then ill do that- level.
#  i cant have levels and fields sets be titled because i check what the file gave is in it, and the file gives lower.
#  the only thing i can do is have in the sets both titled and lowered, and then change prepare file join.
#  either i lower the output of the field, or i make double set of levels, and titled fields

def validate_input(inp, typ):
    """
    validates the type of the input and returns it
    :param inp: str
    :param typ: function
    :return: input
    """

    _input = input(f'Enter {inp} ').title()
    while not typ(_input):
        _input = input(f'Enter {inp} ').title()
        # _input = input(f'Enter {inp} ')
    return _input
    # return _input.title()


#
def vali_date():
    """
    Validates input entered is numbers.
    Tries to create a date object from the input.
    :return: date
    """
    while True:
        year = int(validate_input('year', str.isdecimal))
        month = int(validate_input('month', str.isdecimal))
        day = int(validate_input('day', str.isdecimal)
        try:
            date = datetime.datetime(year, month, day)
            if date <= datetime.datetime.now():
                return date
        except ValueError as w:
            print(w)
        except TypeError as w:
            print(w)


#
def prepare_file(func, field = fields, func2 = None, dic = None):
    """
    checks the file exists.
    creates a reader for the file and checks if its empty. file can have headers or not.
    runs the function
    :param func: function
    :param field: list
    :return: print or function
    """
    while True:
        file = input('Enter file address ').replace('\\', '\\\\')
        # file = re.sub(r'\\', r'\\\\', file)
        try:
            with open(file) as f:
                title = f.readline()
                f.seek(0)
                if title.title() == f"{','.join(field)}\n":
                    field = None

                reader = list(csv.DictReader(f, field, restval=''))
                if not reader:
                    return print('Empty file')
                if not func2:
                    return func(reader)
                return func(reader, func2, dic)
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

# todo make sure user didnt enter commas and shout as well (cause commas have a meaning in csv).
# maybe csv module can handle this

# TODO uncaps everything before putting as a parameter. (or maybe caps everything?) both input here and function.
while True:
    function = input(
        '\nFor ENDING the program type 0.\n\nFor ADDING an employee manually type 1.\nFor ADDING from a FILE type 2.\n'
        'For UPDATING an employee manually type 3.\nFor UPDATING from a FILE type 4.\n'
        'For DELETING an employee manually type 5.\nFor DELETING employees from a FILE type 6.\n'
        'For SEARCHING an employee type 7.\nFor marking your ATTENDANCE type 8.\n'
        'For generating an EMPLOYEE report type 9.\nFor generating current MONTH\'S attendance report type 10.\n'
        'For generating LATE attendance report type 11.\nFor a DATE RANGE attendance report type 12. \n'
        'For a different LEVELS report type 13. \n')
    if comb == 'e':
        break
    if function == '0':
        break
    #     todo test - check level.
    # level
    elif function == '1':
        inputs = []
        for cell in fields:
            check_function = check_field(cell)
            # todo does this work?
            inputs.append(validate_input(cell, check_function))
        line = {fields[index]: inputs[index] for index in range(5)}

        employees.add_employees(line, {inputs[0]})
        # employees.add_employee(employee_id, name, phone, age, level)

    elif function == '2':
        prepare_file(employees.add_employees_from_file, func2= employees.add_employees)

    elif function == '3':
        # todo anna- how do i save the function in another name so its shorter to run next time?
        employee_id = validate_input('employee id', str.isdecimal)
        #todo field. i would need to title the field before the end
        field = validate_input('What field would you like to update: name, phone, age or level?\n',
                               lambda fiel: fiel in fields and fiel != fields[0])
                               # lambda fiel: fiel in fields and fiel != fields[0]).lower()
        check_function = check_field(field)
        # level
        update = validate_input(field, check_function)

        employees.update_employees(update, {employee_id}, field)

    elif function == '4':
        prepare_file(employees.add_employees_from_file, func2= employees.update_employees, dic= {})

    elif function == '5':
        employee_id = validate_input('employee id', str.isdecimal)
        employees.delete_employees({employee_id})

    elif function == '6':
        prepare_file(employees.delete_employees_from_file, ['employee id'])

    # todo test - check search. if exists if not.
    elif function == '7':
        # todo- how to check name?
        emp = validate_input('employee', employees.is_employee)
        # emp = validate_input('employee', lambda char, string: all(char.isalnum() or char.isspace() for char in string))
        # additional = False
        # if input('If you would like employee information, type y. otherwise press ENTER '):
        #     additional = True

        column = fields[1]
        if emp.isdecimal():
            column = fields[0]

        print(employees.search_employee({emp}, column, 'all'))
        # print(employees.NOT_EXIST) if employee_info == 'a' else print(employee_info)
        # print(employees.NOT_EXIST) if not employee_info else print(employee_info)

        # print(f'Employee ID {ID}, {name}, ', additional)

    elif function == '8':
        employee_id = validate_input('employee id', str.isdecimal)
        attendance.mark_attendance(employee_id)

    elif function == '9':
        employee_id = validate_input('employee id', str.isdecimal)

        comb = combining(attendance.employee_attendance_report, employee_id)

        # comb = input(combine)
        # employee_report = attendance.employee_attendance_report(employee_id, comb)
        # if comb:
        #     employee_report, title = employee_report
        #     prepare_reports(employee_report, comb, title)

    elif function == '10':
        comb = combining(attendance.current_month_attendance_report)

        # comb = input(combine)
        # current = attendance.current_month_attendance_report(comb)
        # if comb:
        #     current, title = current
        #     prepare_reports(current, comb, title)

    elif function == '11':
        comb = combining(attendance.late_attendance_report)

        # comb = input(combine)
        # late = attendance.late_attendance_report(comb)
        # if comb:
        #     late, title = late
        #     prepare_reports(late, comb, title)


    # todo test- check different dates.
    elif function == '12':
        # TODO make sure higher than 2021.
        print('Enter From date:')
        _from = vali_date()
        print('Enter Until date:')
        until = vali_date()
        if until < _from:
            until, _from = _from, until
        # until = datetime.datetime(1, 1, 1)
        # while until < _from:
        #     # print('until can not be earlier than from')
        #     print('Enter Until date')
        #     until = check_date()

        comb = combining(attendance.date_range_attendance_report, until, _from)

        # comb = input(combine)
        # ranges = attendance.date_range_attendance_report(until, _from, comb)
        # if comb:
        #     ranges, title = ranges
        #     # is it ok that the from until arent separate?
        #     prepare_reports(ranges, comb, title)
        #     # prepare_reports(ranges, comb, f"{_from} -", str(until))

        # _from = datetime.datetime(2021, 1, 7)
        # until = datetime.datetime(2021, 1, 17)

    # todo test- check all amounts of levels.
    #  new
    elif function == '13':
        # levels = set(
        # levels = []
        # level = (check_str('What level would you like for the report: senior manager, manager, senior or junior? ',
        #                    lambda level: level in employees.levels, 'i')).title()
        # for run in range(2):
        #     more = input('to add more levels type y, to continute press Enter ')
        #     # not sure this the way to do it. how to check enter? '' ,  \n , if not more.isalpha()
        #     if more == '':
        #         break
        #     level = (check_str('What level would you like for the report: senior manager, manager, senior or junior?
        #     ',lambda level: level in employees.levels, 'i')).title()
        #     levels.append(level)
        # attendance.level_attendance_report(levels)

        levels = []
        for run in range(3):
            # not sure this the way to do it. how to check enter? '' ,  \n , if not more.isalpha()
            # level
            level = validate_input('What level would you like for the report: senior manager, manager, senior or '
                                   'junior? \nOr press Enter to continue\n', employees.is_level)
            if level == '':
                break
            levels.append(level)

        comb = combining(attendance.level_attendance_report, levels)

        # comb = input(combine)
        # level = attendance.level_attendance_report(levels, comb)
        # if comb:
        #     level, title = level
        #     prepare_reports(level, comb, title)

    else:
        continue
    # break
