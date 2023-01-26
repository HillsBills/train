import csv


def get_reader(f):
    if not f.read():
        return 0

    f.seek(0)
    reader = csv.DictReader(f, restval=':')
    return reader


class Employees:
    fieldnames = ['employee_id', 'name', 'phone', 'age']
    empty = 'Empty file'
    wrong = 'File is not written according to rules'

    def __init__(self, address):
        self.address = address

    # #TODO mine updating dicts
    # def delete_employees_from_file(self, f2):
    #     # new
    #     reader = get_reader(f2)
    #     if not reader:
    #         return Employees.empty
    #
    #     dicts = self.dict_list()
    #
    #     for row in reader:
    #         # new
    #         if not row['employee_id'].isdigit():
    #             return self.wrong
    #         line = 0
    #         while dicts[line]['employee_id'] != row['employee_id']:
    #             line += 1
    #         dicts.remove(dicts[line])
    #         dicts.remove(line) for line in dicts if line['employee_id'] == row['employee_id']
    #         # for line in dicts:
    #         #     if line['employee_id'] == row['employee_id']:
    #         #         dicts.remove(line)
    #         #         break
    #
    #     self.write_file(dicts)
    #     return 'Deleted'

    # TODO no redundancy, a+
    def delete_employees_from_file(self, f2):
        # new
        reader = get_reader(f2)
        if not reader:
            return self.empty

        for row in reader:
            # new
            if not row['employee_id'].isdigit():
                return self.wrong

        with open(self.address, 'a+', newline='') as f:
            employee_reader = csv.DictReader(f)
            # will this work without creating a list like she did? can i do 'in reader'? no
            # if so then its better than loop in loop no? or in any case i can just make reader a list at the start.
            # also not enough

            dicts = [line for line in employee_reader if line['employee_id'] not in reader]

            f.seek(0)
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)
            return 'Deleted'

    def delete_employee(self, reader):
        with open(self.address, 'a+', newline='') as f:
            employee_reader = csv.DictReader(f)
            dicts = [line for line in employee_reader if line['employee_id'] not in reader]
            f.seek(0)
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)
            return 'Deleted'

    # TODO no redundancy. this is probably better so there is no redundancy.
    def delete_employees(self, employee_ids):
        with open(self.address) as f:
            employee_reader = csv.DictReader(f)
            dicts = [line for line in employee_reader if line['employee_id'] not in employee_ids]
        with open(self.address, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)
            return 'Deleted'

    def delete_employee(self, employee_id):
        print(self.delete_employees([employee_id]))

    def delete_employees_from_file(self, f2):

        reader = get_reader(f2)
        # reader = list(get_reader(f2))
        if not reader:
            return self.empty
        # how do i do this? ignore headers?
        # first = True
        employee_ids = []
        for row in reader:
            # if not first:
            #     if not row[0].isdigit():
            if not row['employee_id'].isdigit():
            # first = False
                return self.wrong
            employee_ids.append(row['employee_id'])

        print(self.delete_employees(employee_ids))

    # TODO one employee does some redundancy
    def delete_employee(self, employee_id):
        print(self.delete_employees([{'employee_id': employee_id}]))

    def delete_employees_from_file(self, f2):

        reader = get_reader(f2)
        if not reader:
            return Employees.empty

        print(self.delete_employees(reader))

    def delete_employees(self, reader):
        # dicts = self.dict_list()
        # with open(self.address, 'a+', newline='') as f:
        with open(self.address) as f:
            dicts = list(csv.DictReader(f))
            for row in reader:
                # new
                if not row['employee_id'].isdigit():
                    return self.wrong
                # am i creating the list over and over?? how did she do it? she didnt do it in a loop.
                #  i can not create a list in a loop. only update it
                # dicts = [line for line in employee_reader if not line['employee_id'] == employee_id]
                # [dicts.remove(line) for line in dicts if line['employee_id'] == row['employee_id']]
                for line in dicts:
                    if line['employee_id'] == row['employee_id']:
                        dicts.remove(line)
                        break
                # this is only good if all ids from deleting match ids from the file
                # line = 0
                # while len(dicts) > 1+line and dicts[line]['employee_id'] != row['employee_id']:
                #     line += 1
                # dicts.remove(dicts[line])

        with open(self.address, 'w', newline='') as f:
            # self.write_file(dicts)
            # not sure i need this? will 'write' delete everything with append?
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)
            return 'Deleted'

    # def dict_list(self):
    #     with open(self.address) as f:
    #         return list(csv.DictReader(f))
    #
    # def write_file(self, dicts):
    #     with open(self.address, 'w', newline='') as f1:
    #         writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
    #         writer.writeheader()
    #         writer.writerows(dicts)

# ---------------------------------------------------------------from employee delete-------------------------------



   # only check. or function for the whole thing.
    def delete_employees(self, employee_ids):
        # employee_reader= self.dict_list()
        with open(self.address) as f:
            employee_reader = list(csv.DictReader(f))

        # option #1
        [employee_reader.remove(line) for line in employee_reader if line['employee_id'] in employee_ids]
        # for employee in employee_reader:
        #     if employee['employee_id'] in employee_ids:
        #         employee_reader.remove(employee)

        # option #2- sometimes not updating things but creating them new, means less mistakes in a system.
        # not in, is in order to unify one argument with a list. (in instead of ==)
        # maybe i can do it with 2 fors like my way? but will it be sensfull and not duplicate the for?
        dicts = [line for line in employee_reader if line['employee_id'] not in employee_ids]
        # f.close()
        # basically she said there is no way to unify them in the same for. so she made two in order to unify functions
        # self.write_file(dicts)
        with open(self.address, 'w', newline='') as f1:
            writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)

    def delete_employees(self, employee_ids):
        with open(self.address) as f:
            employee_reader = list(csv.DictReader(f))

        for row in reader:
            if not row['employee_id'].isdigit():
                return self.wrong
            # i dont think i need []
            [dicts.remove(line) for line in dicts if line['employee_id'] == row['employee_id']]

        # option #2- sometimes not updating things but creating them new, means less mistakes in a system.

        dicts = [line for line in employee_reader if line['employee_id'] not in employee_ids]

        with open(self.address, 'w', newline='') as f1:
            writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(dicts)

    def delete_employee(self, employee_id):
        # function. params- equal to, function of for, id\file.
        # should i do 2 inside functions? with a middle?
        # employee_reader, f = self.dict_list()
        # dicts = [line for line in employee_reader if not line['employee_id'] == employee_id]
        # f.close()
        # self.write_file(dicts)
        self.delete_employees([employee_id])

    def delete_employees_from_file(self, f2):
        # new
        reader = check_empty(f2)
        if not reader:
            return self.empty

        ids_to_delete = []

        # employee_reader, f = self.dict_list()
        # dicts = [line for line in employee_reader]
        # f.close()

        for row in reader:
            # new
            if not row['employee_id'].isdigit():
                return self.wrong
            ids_to_delete.append(row['employee_id'])
            # [dicts.remove(line) for line in dicts if line['employee_id'] == row['employee_id']]

        # self.write_file(dicts)
        self.delete_employees(ids_to_delete)
        return 'Deleted'

    # def write_file(self, dicts):
    #     with open(self.address, 'w', newline='') as f1:
    #         writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
    #         writer.writeheader()
    #         writer.writerows(dicts)

    # # in order to avoid close outside of the function, i can transfer the reader into a list and just return the list,
    # # without f
    # def dict_list(self):
    #     with open(self.address) as f:
    #         return list(csv.DictReader(f))
    #     # employee_reader = csv.DictReader(f)
    #     # return employee_reader, f
    #
    # @staticmethod
    # def check_empty(f):
    #
    #     if not f.read():
    #         return 0, 'Empty file'
    #
    #     else:
    #         f.seek(0)
    #         wrong = 'File is not written according to rules'
    #         reader = csv.DictReader(f, restval=':')
    #         return wrong, reader
    #
    # # save checkfile in a var. if the var isnt empty, return it. else, do the function.
    # @staticmethod
    # def check_file(row, wrong):
    #     # for row in reader:
    #         # new
    #     if not row['employee_id'].isdigit():
    #         return wrong
    #
    # #inorder to change the ifs parameter the ifs need to be in an extra function which will be a parameter
    # # in the helper function (3 functions)
    #
    # def delete_employee(self, employee_id=None, reader=None, wrong=None):
    #     """
    #     Will delete an employee from the Employee file
    #     :param employee_id: int
    #     # :return:
    #     """
    #
    # if not f.read():
    #     return 'Empty file'
    #
    # else:
    #     f.seek(0)
    #     wrong = 'File is not written according to rules'
    #     reader = csv.DictReader(f, restval=':')
    #
    #     with open(self.address) as f:
    #         f.seek(0)
    #         employee_reader = csv.DictReader(f)
    #         # maybe list comprehension
    #         dicts = []
    #
    # for line in employee_reader:
    #     if not line['employee_id'] == employee_id:
    #         self.dicts.append(line)
    #
    # if wrong:
    #     for row in reader:
    #             # new
    #         employee_id = row['employee_id']
    #         if not row['employee_id'].isdigit():
    #             return wrong
    #         for line in employee_reader:
    #             if not line['employee_id'] == employee_id:
    #                 dicts.append(line)
    #
    #
    #     with open(self.address, 'w', newline='') as f1:
    #         writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
    #         writer.writeheader()
    #         writer.writerows(dicts)
    #
    # def del_file(self):
    # # delete
    # wrong, reader = self.check_empty(f2)
    # if not wrong:
    #     return reader
    #
    # self.delete_employee(reader=reader, wrong=wrong)
    #
    # with open(self.address) as f:
    #     f.seek(0)
    #     employee_reader = csv.DictReader(f)
    #     # maybe list comprehension
    #     dicts = []
    #     for line in reader:
    #         # new
    #         if not line['employee_id'].isdigit():
    #             return wrong
    #         # old and new
    #         for row in employee_reader:
    #             if not row['employee_id'] == line['employee_id']:
    #                 dicts.append(line)
    #
    # # old and new
    # # f.seek(0)
    # for line in employee_reader:
    #     if line['employee_id'] == row['employee_id']:
    #         self.dicts.remove(line)
    #
    # for row in reader:
    #     # new
    #     if not row['employee_id'].isdigit():
    #         return self.wrong
    #     for line in self.dicts:
    #         if line['employee_id'] == row['employee_id']:
    #             self.dicts.remove(line)
    #
    # with open(self.address, 'w', newline='') as f1:
    #     writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
    #     writer.writeheader()
    #     writer.writerows(dicts)
    #
    #         # f.seek(0)
    #         # for line in reader:
    #         #     print(line)
    #         #     if reader.line_num == 4:
    #
    # def add_employee(self, employee_id, name, phone, age):
    #
    # with open(self.address, 'a', newline='') as f:
    #     writer = csv.DictWriter(f, fieldnames=self.fieldnames)
    #     writer.writerow({'employee_id': employee_id, 'name': name, 'phone': phone, 'age': age})

address_e = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv'
employee = Employees(address_e)
employee.delete_employee('1')
# with open('data/Delete employees.csv') as f:
#     print(employee.delete_employees_from_file(f))