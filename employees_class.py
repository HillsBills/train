import file
import csv


# def get_reader(f, fields):
#     """
#     returns a dict reader which can be empty. file can have headers or not
#     :param f: file
#     :param fields: list
#     :return: reader
#     """
#     line = f.readline()
#     f.seek(0)
#     #
#     if line == f"{','.join(fields)}\n":
#         fields = None
#     return list(csv.DictReader(f, fields, restval=':'))


class Employees:
    fieldnames = ['employee_id', 'name', 'phone', 'age', 'level']
    # empty = 'Empty file'
    wrong = 'File is not written according to rules'
    # exists = 'Employee already exists'
    not_exist = "doesn't exist in the file"
    levels = {'', 'senior manager', 'manager', 'senior', 'junior'}

    #      check if file exists? should i assert an error and crash the program? or use the programs error
    #  with read or something with try raise. yes raise an error and crash if the file is empty. (open read and if None)
    # or the wrong type file. (check its csv with a real command). or check written like csv
    # (create it only if it doesnt exist.)
    def __init__(self, address):
        """
        Will initiate the address to the object.
        creates a list of employee reader which will be empty if the file doesnt exist (and set mode to w),
        or employees were deleted
        :param address: str
        """
        #
        self.address = address

        try:
            with open(address) as f1:
                self.employee_reader = list(csv.DictReader(f1))
        except FileNotFoundError:
            self.employee_reader = []

    #  (Create a search function - only for the challenge. will search for the id before and shout if exists.)
    # create a table where every comma is a new column and every enter is a new line.
    # when writing in the file dont add any unnecessary spaces. this isnt a free style writing, it is precise
    #  the file either doesnt exist because i didnt add to it yet, or only the header exists because i deleted all.
    # i cant have a situation where there is no header. its my file, im controlling it. the address has to be correct.
    # i cant handle if a file exists somewhere else. how will i know

    def _add(self, lines, employee_ids):
        """
        add to file helper function
        if file exists, will make sure employee doesn't exist already.
        writes employees to the employee file
        :param lines: list
        :param employee_ids: list
        :return print
        """
        mode = 'w'
        if self.employee_reader:
            mode = 'a'
            _id = self.search_employee(employee_ids)
            if _id:
                #
                return print(f'{_id} employee exists in the file')

        file.write_file(lines, self.address, self.fieldnames, mode)

    def add_employee(self, employee_id, name, phone, age, level=None):
        """
        Will add a new employee to the Employee file.
        creates the employee dictionary
        runs the add helper for one employee
        :param employee_id: str
        :param name: str
        :param phone: str
        :param age: str
        :param level: str
        """
        line = [{'employee_id': employee_id, 'name': name, 'phone': phone, 'age': age, 'level': level}]
        self._add(line, [employee_id])

    # if I wish to add an employee where the id is equal, I will check if the name is equal,
    # if so print exists and continue. Else stop everything. (don’t continue to write)
    # If this is too complicated then just stop everything and say the id exists.
    def add_employees_from_file(self, reader):
        """
        Will add new employees to the Employee file, using a file. The file can contain none, one or more employees.
        makes sure all cells are writen properly.
        makes a list of employee ids
        changes the reader to upper case
        runs the add helper for all employees
        :param reader: list
        :return: print
        """
        # i can try and raise empty. no, its not an error
        # and we i succeed then i do the rest.
        # until the for i will use a function
        #  self or Employee?
        # reader = get_reader(reader, Employees.fieldnames)
        # if not reader:
        #     return print(Employees.empty)

        # (again if the name is the same then its ok to skip and not write it, instead of not doing anything.
        # If its easy I will do this)
        #
        employee_ids = []
        for line in reader:
            # inorder to change the ifs parameter the ifs need to be in an extra function which will be a parameter
            # in the helper function (3 functions) (to use in function 4)
            if not line['employee_id'].isdigit() or not line['name'].isalpha() or not line['phone'].isdigit() \
                    or not line['age'].isdigit() \
                    or not line['level'] in Employees.levels or line['employee_id'] in employee_ids:
                return print(Employees.wrong)
            employee_ids.append(line['employee_id'])
            line['name'], line['level'] = line['name'].title(), line['level'].title()

        self._add(reader, employee_ids)

        # or not line['name'].islower()
        #     lines.append([{'employee_id': line['employee_id'], 'name': line['name'].lower(), 'phone': line['phone'],
        #                   'age': line['age']}])
        # #     and write lines instead of reader
        # with a regular read and write?
        # is there a better way? write the function again

        # if i put it in a list i wont need seek, plus memory wise is better to look at a list rather than a file:
        # for, if not not not, append line. how does any all filter help me here?
        # f.seek(0)
        # # to read the title again...instead of next
        # reader = csv.DictReader(f)

        # next(reader)

    def _delete(self, employee_ids):
        """
        delete from file helper function
        creates a list of dictionaries not to delete
        makes sure there are ids to delete in the employee file
        rewrites the file with the dict list (without the deleted ids)
        :param employee_ids: set
        :return: print
        """
        # with open(self.address) as f:
        #     employee_reader = list(csv.DictReader(f))
        dicts = [line for line in self.employee_reader if line['employee_id'] not in employee_ids]
        if self.employee_reader == dicts:
            return print(Employees.not_exist)

        file.write_file(dicts, self.address, self.fieldnames)

        # with open(self.address, 'w', newline='') as f:
        #     writer = csv.DictWriter(f, fieldnames=self.fieldnames)
        #     writer.writeheader()
        #     writer.writerows(dicts)
        #     return 'Deleted'

    def delete_employee(self, employee_id):
        """
        Will delete an employee from the Employee file
        runs the delete helper for one employee
        :param employee_id: str
        """
        self._delete({employee_id})

    #  if you try to delete an id that doesn’t exist then it will print it doesn’t exist but will continue.
    #  This is complicated. If its not that important then I wont do it.
    #  Right now I don’t check if ids exist the other way round.
    def delete_employees_from_file(self, reader):
        """
        Will delete an employee from the Employee file using a file. The file may contain no, one or more employees.
        makes sure cells are writen properly.
        makes a list of employee ids
        runs the delete helper for all employees
        :param reader: list
        :return: print
        """
        # reader = get_reader(reader, ['employee_id'])
        # if not reader:
        #     return print(Employees.empty)

        employee_ids = set()
        for row in reader:
            if not row['employee_id'].isdigit():
                return print(Employees.wrong)
            employee_ids.add(row['employee_id'])

        self._delete(employee_ids)

    # TODO add the searches to all the functions. if there is a problem write a message. with add dont add nothing.
    # besides delete from file. return true immediately when found
    # not in, needs to be clean.
    # if list for reader exists?
    # do the same way? prob yes

    # does this work when file is empty? or error. works
    # add a check in main that its alpha
    #
    def search_employee(self, category):

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
        for line in self.employee_reader:
            if line[column] in category:
                return line["employee_id"], line["name"], f'Phone {line["phone"]}, Age {line["age"]}'

    #
    def search_employee(self, category, name=None, additional=None):
        """
        searches for an employee id\name. returns true\f or returns additional info\name
        :param name: boolean
        :param additional: boolean
        :param category: list
        :return: if additional, name =None, return true/ None. Otherwise return additional\name.
        """
        #  add option for a set of levels that will collect a set of ids and later return it.
        #  maybe i return all in a tuple and take what i need in the other function.
        #  and the second thing would be a set of ids. maybe dont have catagory but write the field.
        #  change the print where you run the search func.
        column = 'name'
        if category[0].isdigit():
            # if category.copy().pop().isdigit():
            column = 'employee_id'

        # emp = set()
        # for line in self.employee_reader:
        #     emp.add(line[column])
        category = set(category)

        # if emp.intersection(category):
        for line in self.employee_reader:
            if line[column] in category:
                if name:
                    return line["name"]
                elif additional:
                    return f'Employee ID {line["employee_id"]}, {line["name"]}, Phone {line["phone"]},' \
                           f' Age {line["age"]}, {line["level"]}'
                else:
                    return f'{line[column]} employee exists in the file'

    # def write_file(self, param, mode):
    #     with open(self.address, mode, newline='') as f2:
    #         writer = csv.DictWriter(f2, fieldnames=self.fieldnames, extrasaction='ignore')
    #         if mode == 'w':
    #             writer.writeheader()
    #         writer.writerows(param)
    #         return 'done'

    # def append_file(self, param):
    #     with open(self.address, newline='') as f2:
    #         writer = csv.DictWriter(f2, fieldnames=self.fieldnames, extrasaction='ignore')
    #         writer.writerows(param)
    #         return 'copied'


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
