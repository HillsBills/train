import file

ADDRESS = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv'
FIELDNAMES = ['Employee Id', 'Name', 'Phone', 'Age', 'Level']
fieldnames = [field.lower() for field in FIELDNAMES]
# FIELDNAMES = ['employee id', 'name', 'phone', 'age', 'level']
WRONG = 'File is not written according to rules'
NOT_EXIST = "doesn't exist in the file"


# do i need the empty cell here? why? because im allowing not to enter a level, and im checking the level is valid
# LEVELS = {'', 'senior manager', 'manager', 'senior', 'junior'}


#     TODO check if file exists? should i assert an error and crash the program? or use the programs error
#  with read or something with try raise. yes raise an error and crash if the file is empty. (open read and if None)
# or the wrong type file. (check its csv with a real command). or check written like csv
# (create it only if it doesnt exist.)

# TODO: (Create a search function - only for the challenge. will search for the id before and shout if exists.)
# create a table where every comma is a new column and every enter is a new line.
# when writing in the file dont add any unnecessary spaces. this isnt a free style writing, it is precise
# TODO: the file either doesnt exist because i didnt add to it yet, or only the header exists because i deleted all.
# i cant have a situation where there is no header. its my file, im controlling it. the address has to be correct.
# i cant handle if a file exists somewhere else. how will i know
# todo test- search works when exists and when doesnt.
#  -check when user exists and doesnt

def is_level(lev):
    return lev in {'', 'senior manager', 'senior manager'.title(), 'manager', 'manager'.title(), 'senior',
                   'senior'.title(), 'junior', 'junior'.title()}
    # return lev in {'', 'senior manager', 'manager', 'senior', 'junior'}


def is_employee(employee, name=None):
    func = str.isalnum
    if name:
        func = str.isalpha

    if all(func(char) or char.isspace() for char in employee) and len(employee) >= 2:
        return True
    return False


def is_name(employee):
    return is_employee(employee, 1)


# todo test- check level yes no
# todo new
def add_employees(lines, employee_ids):
    """
    add to file helper function
    if file exists, will make sure employee doesn't exist already.
    writes employees to the employee file
    :param lines: list
    :param employee_ids: list
    :return print
    """

    mode = search_employee(employee_ids, FIELDNAMES[0])
    if mode == NOT_EXIST:
        mode = 'a'
    # if mode != 'w' and mode:  # this work? mode!=[] ?
    elif mode != 'w':  # this work? mode!=[] ?
        return print(mode)

    file.write_file(lines, ADDRESS, FIELDNAMES, mode)


# def add_employee(employee_id, name, phone, age, level=None):
#     """
#     Will add a new employee to the Employee file.
#     creates the employee dictionary
#     runs the add helper for one employee
#     :param employee_id: str
#     :param name: str
#     :param phone: str
#     :param age: str
#     :param level: str
#     """
#     line = [{'employee_id': employee_id, 'name': name, 'phone': phone, 'age': age, 'level': level}]
#     _add(line, [employee_id])

# todo- should i check if there are  extra fields? does it disturb me if i copy it to the file?
#  dont think it disturbs. can check. does resval take care of it?
def add_employees_from_file(reader, function, dic=None):
    employee_ids = set()
    # dic={}
    for line in reader:
        # level
        #  todo- how to check name?
        if not line[fieldnames[0]].isdecimal() or not is_name(line[fieldnames[1]])\
                or not line[fieldnames[2]].isdecimal() or not line[fieldnames[3]].isdecimal() \
                or not is_level(line[fieldnames[4]]) or line[fieldnames[0]] in employee_ids:
        # if not line[FIELDNAMES[0]].isdecimal() or not is_name(line[FIELDNAMES[1]])\
        #     or not line[FIELDNAMES[2]].isdecimal() or not line[FIELDNAMES[3]].isdecimal() \
        #     or not is_level(line[FIELDNAMES[4]]) or line[FIELDNAMES[0]] in employee_ids:
            # if not line['employee_id'].isdecimal() or not line['name'].isalpha() or not line['phone'].isdecimal() \
            #     or not line['age'].isdecimal() \
            #     or not line['level'] in LEVELS or line['employee_id'] in employee_ids:
            return print(WRONG)
        employee_ids.add(line[fieldnames[0]])
        # todo anna- how can i run the same function on 2 params the same time. can i do this with map?
        #  maybe only on params
        line[fieldnames[1]], line[fieldnames[4]] = line[fieldnames[1]].title(), line[fieldnames[4]].title()
        # dic['1'] = line
        if dic == {}:
            dic[line[fieldnames[0]]] = line
    # instead of a list of lines, i will have a dict of lines
    if dic:
        reader = dic

    function(reader, employee_ids)


def update_employees(update, employee_ids, field=None):
    employee_reader = file.get_reader(ADDRESS)
    update_reader = []
    for line in employee_reader:
        if line[FIELDNAMES[0]] in employee_ids:
            # todo anna- is there a better way to combine the functions?
            if field:
                line[field] = update
            else:
                # dic['1']
                line = update[line[FIELDNAMES[0]]]
        update_reader.append(line)

    if employee_reader == update_reader:
        return print(f'{NOT_EXIST} or no update')

    file.write_file(update_reader, ADDRESS, FIELDNAMES)


# if I wish to add an employee where the id is equal, I will check if the name is equal,
# if so print exists and continue. Else stop everything. (don’t continue to write)
# If this is too complicated then just stop everything and say the id exists.
# todo test- all ifs.
#  -capitalizing works
# def add_employees_from_file(reader):
#     """
#     Will add new employees to the Employee file, using a file. The file can contain none, one or more employees.
#     makes sure all cells are writen properly.
#     makes a list of employee ids
#     changes the reader to upper case
#     runs the add helper for all employees
#     :param reader: list
#     :return: print
#     """
#     # i can try and raise empty. no, its not an error
#     # and we i succeed then i do the rest.
#     # until the for i will use a function
#     # TODO self or Employee?
#
#     # (again if the name is the same then its ok to skip and not write it, instead of not doing anything.
#     # If its easy I will do this)
#     #
#     employee_ids = set()
#     for line in reader:
#         # inorder to change the ifs parameter the ifs need to be in an extra function which will be a parameter
#         # in the helper function (3 functions) (to use in function 4)
#         #  todo- how to check name?
#         if not line['employee_id'].isdecimal() or not line['name'].isalpha() or not line['phone'].isdecimal() \
#                 or not line['age'].isdecimal() \
#                 or not line['level'] in LEVELS or line['employee_id'] in employee_ids:
#             return print(WRONG)
#         employee_ids.add(line['employee_id'])
#         # todo anna- how can i run the same function on 2 params the same time. can i do this with map?
#         #  maybe only on params
#         line['name'], line['level'] = line['name'].title(), line['level'].title()
#
#     add_employees(reader, employee_ids)

# #     and write lines instead of reader
# with a regular read and write?
# is there a better way? write the function again

# if i put it in a list i wont need seek, plus memory wise is better to look at a list rather than a file:
# for, if not not not, append line. how does any all filter help me here?


# # todo new
# def _add(lines, employee_ids):
#     """
#     add to file helper function
#     if file exists, will make sure employee doesn't exist already.
#     writes employees to the employee file
#     :param lines: list
#     :param employee_ids: list
#     :return print
#     """
#
#     mode = search_employee(employee_ids)
#     if not mode:
#         mode = 'a'
#     if mode != 'w' and mode:  # this work? mode!=[] ?
#         return print(mode)
#
#     file.write_file(lines, ADDRESS, FIELDNAMES, mode)


def _old_add(lines, employee_ids):
    mode = 'w'
    if file.get_reader(ADDRESS):
        mode = 'a'
        _id = search_employee(employee_ids)
        if _id:
            #
            # return print(f'{_id} employee exists in the file')
            return print(_id)
    file.write_file(lines, ADDRESS, FIELDNAMES, mode)


# todo test- check when exists and when doesnt.
def delete_employees(employee_ids):
    """
    delete from file helper function
    creates a list of dictionaries not to delete
    makes sure there are ids to delete in the employee file
    rewrites the file with the new dict list (without the deleted ids)
    :param employee_ids: set
    :return: print
    """
    employee_reader = file.get_reader(ADDRESS)
    lines = [line for line in employee_reader if line[FIELDNAMES[0]] not in employee_ids]
    if employee_reader == lines:
        return print(NOT_EXIST)

    file.write_file(lines, ADDRESS, FIELDNAMES)


# def delete_employee(employee_id):
#     """
#     Will delete an employee from the Employee file
#     :param employee_id: str
#     """
#     delete_employees({employee_id})


#  if you try to delete an id that doesn’t exist then it will print it doesn’t exist but will continue.
#  This is complicated. If its not that important then I wont do it.
#  Right now I don’t check if ids exist the other way round.
# todo test - check when exists and not
def delete_employees_from_file(reader):
    """
    Will delete an employee from the Employee file using a file. The file may contain no, one or more employees.
    makes sure cells are writen properly.
    makes a list of employee ids
    :param reader: list
    :return: print
    """
    employee_ids = set()
    for row in reader:
        if not row[fieldnames[0]].isdecimal():
            return print(WRONG)
        employee_ids.add(row[fieldnames[0]])

    delete_employees(employee_ids)


# not sure the extra if is worth it.
# todo test- check 2 returns work. when not exist and when do.
# TODO in the end i can have a search algorithm- the ids by order and i half every time and check if bigger or smaller.
def search_employee(employees, column, additional=None):
    """
    searches for an employee id\name. returns true\f or returns additional info\name and level
    :param column: str
    :param employees: list
    :param additional: int
    :return: if extra =None, return true/ None. Otherwise return additional \name+ level.
    uses: searches for name from id in Attendance.
    searches for id from id/s in Employee.
    searches for info or true from id or name in Main. or always give information.
    """
    # todo- (add option for a set of levels that will collect a set of ids and later return it.
    #  maybe i return all in a tuple and take what i need in the other function.
    #  and the second thing would be a set of ids. maybe dont have catagory but write the field.
    #  change the print where you run the search func.)

    # column = 'name'
    # if employees[0].isdigit():
    #     column = 'employee_id'

    employee_reader = file.get_reader(ADDRESS)
    # can delete this part if i dont like the added if
    if not employee_reader:
        return 'w'

    # employees = set(employees)

    for line in employee_reader:
        # this can happen only once
        if line[column] in employees:
            if additional == 'name':
                # for mark attendance
                return line[FIELDNAMES[1]], line[FIELDNAMES[4]]
                # return line["Name"], line["Level"]
            elif additional == 'all':
                # for search employee
                return f'Employee ID {line[FIELDNAMES[0]]}, {line[FIELDNAMES[1]]}, Phone {line[FIELDNAMES[2]]},' \
                       f' Age {line[FIELDNAMES[3]]}, {line[FIELDNAMES[4]]}'
                # return f'Employee ID {line["employee_id"]}, {line["name"]}, Phone {line["phone"]},' \
                #        f' Age {line["age"]}, {line["level"]}'
            else:
                # for add employee
                return f'{line[column]} employee exists in the file'
    # return 'a'
    return NOT_EXIST


# for multiple searches of levels, and singular for others
def search_employees(param, extra=None):
    if param[0].isdigit():
        column = 'employee_id'
    elif param[0] in LEVELS:
        column = 'level'
    else:
        column = 'name'

    param = set(param)
    employee_reader = file.get_reader(ADDRESS)
    ids = set()

    if extra == 1:
        for line in employee_reader:
            if line[column] in param:
                ids.add(line["employee_id"])
        return ids
    else:
        for line in employee_reader:
            if line[column] in param:
                if not extra:
                    return f'{line[column]} employee exists in the file'
                elif extra == 2:
                    return line["name"], line["level"]
                else:
                    return f'Employee ID {line["employee_id"]}, {line["name"]}, Phone {line["phone"]},' \
                           f' Age {line["age"]}, {line["level"]}'

    # old version. why isnt this better? because of 2 ifs in the for?
    for line in employee_reader:
        if line[column] in param:
            if extra == 1:
                ids.append(line["employee_id"])
            elif not extra:
                return f'{line[column]} employee exists in the file'
            elif extra == 2:
                return line["name"]
            else:
                return f'Employee ID {line["employee_id"]}, {line["name"]}, Phone {line["phone"]},' \
                       f' Age {line["age"]}, {line["level"]}'
    return ids


# TODO add the searches to all the functions. if there is a problem write a message. with add dont add nothing.
# besides delete from file. return true immediately when found
# not in, needs to be clean.
# if list for reader exists?
# do the same way? prob yes

# does this work when file is empty? or error. works
# add a check in main that its alpha

#
def search_employeeold(category):
    # search searches for name from id in attendance.
    # searches for id from id/s in employee.
    # searches for info or true from id or name in main. or always give information.

    # column = 'employee_id'
    # if name:
    #     column = 'name'

    column = 'name'
    if category[0].isdigit():
        # if category.copy().pop().isdigit():
        column = 'employee_id'

    # emp = set()
    # for line in self.employee_reader:
    #     emp.add(line[column])
    category = set(category)
    #
    # if emp.intersection(category):
    for line in employee_reader:
        if line[column] in category:
            return line["employee_id"], line["name"], f'Phone {line["phone"]}, Age {line["age"]}'

    # todo anna- in order to combine with delete from file, i can make the ifs into a function.
    #  the function would try every field, and if succeeds, would make the right type of check.
    #  i can use the function also in main, where if i get a wrong, i ask for input again.
    #  how do i go over every field, without having a reader? how do i compare between reader and input string?
    #  the for needs to be external. i can leave main out of this option. and not have an extra function.
    #  how can i do try except where he will ignore the non existing key and just continue? can i go over each cell?
    #  i can make a for by for for the headers, have a function that checks the header and gives back the function.
    #  but what shall i do with the function for level?
    employee_ids = set()
    for row in reader:
        if not row['employee_id'].isdecimal():
            return print(WRONG)
        employee_ids.add(row['employee_id'])

    delete_employees(employee_ids)


def validate_field(header):
    employee_reader = file.get_reader(ADDRESS)
    new_reader = []

    for line in employee_reader:
        if line[FIELDNAMES[0]] in employee_ids:
            line = dic[line[FIELDNAMES[0]]]
        new_reader.append(line)

    file.write_file(new_reader, ADDRESS, FIELDNAMES)

    employee_reader = file.get_reader(ADDRESS)
    new_reader = []

    for line in employee_reader:
        for row in reader:
            if line[FIELDNAMES[0]] == row[FIELDNAMES[0]]:
                line = row
            new_reader.append(line)

    file.write_file(new_reader, ADDRESS, FIELDNAMES)


def update_employees_file(employee_id, field, update):
    employee_reader = file.get_reader(ADDRESS)
    new_reader = []
    for line in employee_reader:
        if line[FIELDNAMES[0]] == employee_id:
            line[FIELDNAMES[field]] = update
        new_reader.append(line)

    if employee_reader == new_reader:
        return print(f'{NOT_EXIST} or no update')

    file.write_file(new_reader, ADDRESS, FIELDNAMES)

# chuck = Employees('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv')
# chuck.add_employee('15', 'hilla', '9', '10')
# print(chuck.search_employee(['6']))
# f = open('data/Delete employees.csv')
# chuck.something(f)
# f = open('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Add employees.csv')
# print(chuck.add_employees_from_file(f))
# f.close()
# print(chuck.delete_employee('6'))
# print(chuck.delete_employees_from_file(f))
# f.close()
# chuck._delete({'7'})
