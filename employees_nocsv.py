import re

class Employees:

    #     TODO check if file exists? should i assert an error and crash the program? or use the programs error
    #  with read or something with try raise
    def __init__(self, address):
        """
        Will initiate the address to the object, so every function has the address
        :param address: str
        """
        self.address = address

    # TODO: (Create a search function - only for the challenge. will search for the id before and shout if exists.)
    # TODO create a table where every comma is a new column and every enter is a new line.
    # when writing in the file dont add any unnecessary spaces. this isnt a free style writing, it is precise
    def add_employee(self, employee_id, name, phone, age):
        """
        Will add a new employee to the Employee file.
        :param employee_id: int
        :param name: str
        :param phone: int
        :param age: int
        #:return:

        -open and write to the file with commas
        """

        with open(self.address, 'a+') as f:
            # f.read()
            f.write(f'{employee_id},{name},{phone},{age}\n')

    def add_employees_from_file(self, f):
        """
        Will add new employees to the Employee file, using a file. The file can contain none, one or more employees.
        :param f: str
        :return: message for success or failure

        -if the file is empty say its empty and finish function. (read and if None)
        -if the file isnt empty, check that every line has all needed categories
            and that they are the correct type by order. (maybe readline, (or re)
            split lines with ',' in order to have the different cells, check type of each list entry,)
            shout all needed information in the file, and its order if there is a problem)
        -in a while, readline, open and write to employee file
        """

        if not f.read():
            f.close()
            return 'Empty file'
        else:
            wrong = 'File is not written according to rules'
            f.seek(0)
            f.readline()
            for line in f:
                employee = line.strip().split(',')
                # employee = next(f)
                # print(employee, end='')
                if len(employee) != 4 or not employee[0].isdigit() or not employee[1].isalpha() or \
                        not employee[2].isdigit() or not employee[3].isdigit():
                    f.close()
                    return wrong

            f.seek(0)
            f.readline()
            with open(self.address, 'a+') as f1:
                # f1.read()
                for line in f:
                    f1.write(line)
                f1.write('\n')
                f.close()
                return 'copied'

    def delete_employee(self, employee_id):
        """
        Will delete an employee from the Employee file
        :param employee_id: int
        # :return:

        -check entered is an int.
        -open read and write employee file. find employee id (method? re? go over columns?) find with read and string
             method. readline. write with replace '' with the line. maybe also end=''
        -delete line where found (equal line to None? but the line will be empty, it needs to not exist.
        replace? sub? changes the file?
            ofir suggested to copy all but the line to a new file and delete previous file.
            no need, just rewrite the new file )
        """

        with open(self.address, 'a+') as f:
            f.seek(0)
            string = re.search(rf'{employee_id},\w* \w*,\d*,\d*',f.read())
            # print(f.read())
            f.seek(0)
            i = f.read().find(string.group())
            f.seek(i)
            # line = f.readline()
            # f.seek(i)
            # f.write(f.readline().replace(string.group(),'',1))
            # no good. need to do like ofir cause it is a var.
            f.write(string.group().replace(string.group(),'',1))

            # f.write(f.read().replace(f.readline(),''))
            # f.write(f'{employee_id},{name},{phone},{age}\n')

            # with open(self.address) as f:
            #     f.seek(0)
            #     reader = csv.DictReader(f)
            #     # for line in reader:
            #     #     print(line)
            #     with open(self.address, 'w') as f1:
            #         # writer = csv.DictWriter(f1, fieldnames=self.fieldnames)
            #         # writer.writeheader()
            #         for line in reader:
            #             print(line,'2')

            '''save all read
            open the file for write
            iterate over read
            when finding the id in writerow skip the write.'''

            # with open(self.address) as f:
            #     f.seek(0)
            #     reader = csv.reader(f)
            #     dicts = []
            #     for line in reader:
            #         dicts.append(line)
            # print(dicts)

            # with open(self.address, 'w', newline='') as f1:
            #     writer = csv.writer(f1)
            #     for line in dicts:
            #         if line[0] == employee_id:
            #             line = ''
            #             print(dicts)
            #             break

    def delete_employees_from_file(self, file_address):
        """
        Will delete an employee from the Employee file using a file. The file may contain no, one or more employees.
        :param file_address: str
        # :return:

        -check file address is valid.
            (check file exists with open read or something with try except and break to main while)
        -if the file is empty say its empty and finish function. (read and if None)
        -make sure all is commas and ints. and make sure every line has one int.
            shout that the file shouldnt contain non ints, and that every line should have one int.
        -in a while, copy each int (split lines with ',' in order to have the different cells)
            open and read and write to employee file.
            find employee id (method? re? go over columns?)
        -delete line where found (equal line to None? but the line will be empty, it needs to not exist)
            ofir suggested to copy all but the line to a new file and delete previous file)
        """
        pass

    def delete_employee(self, employee_id):
        employee_reader, f = self.dict_list()
        dicts = [line for line in employee_reader if not line['employee_id'] == employee_id]
        f.close()
        self.write_file(dicts)


    def delete_employees_from_file(self, f2):
        reader = check_empty(f2)
        if not reader:
            return self.empty

        employee_reader, f = self.dict_list()
        dicts = [line for line in employee_reader]
        f.close()

        for row in reader:
            # new
            if not row['employee_id'].isdigit():
                return self.wrong
            [dicts.remove(line) for line in dicts if line['employee_id'] == row['employee_id']]

        self.write_file(dicts)



chuck = Employees('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv')
# chuck.add_employee('8','hilla','9','10')
f = open('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Add employees.csv')
print(chuck.add_employees_from_file(f))
