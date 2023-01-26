import datetime
import csv
import employees_class
import file


class Attendance:
    fieldnames = ['date', 'time', 'employee_id', 'name']

    #     TODO check if file exists? should i assert an error and crash the program? or use the programs error
    # TODO if i need employee only in one function, i wont add it in init but in the function.
    def __init__(self, address):
        """
        Will initiate the address to the object
        creates a list of reader which will be empty if the file doesnt exist yet
        :param address: str
        """
        self.address = address
        self.report = []

        try:
            with open(self.address) as f:
                self.reader = list(csv.DictReader(f))
        except FileNotFoundError:
            self.reader = []

    def mark_attendance(self, employee_id, employee):
        """
        given an employee id, writes an attendance log to the attendance file
        Will check the employees_file for the employee_id. (and will take the name).
        if the file exists, will change write mode to append
        Will write date, time, id and name entry to the attendance log.
        :param employee_id: str
        :param employee: Employees
        :return: message
        """
        name = employee.search_employee({employee_id})
        if not name:
            return f'{employee_id} {employee.NOT_EXIST}'

        mode = 'w'
        if self.reader:
            mode = 'a'

        time = datetime.datetime.now().strftime("%X")
        date = datetime.datetime.now().strftime("%x")
        param = [{'date': date, 'time': time, 'employee_id': employee_id, 'name': name}]
        return file.write_file(param, self.address, self.fieldnames, mode)
        # return 'Attendance marked'

    def employee_attendance_report(self, employee_id):
        """
        Given an employee id, will return all its attendance entries.
        creates a list of lines for the report
        :param employee_id: str
        :return: attendance entry report from the log with this id, header
        """

        [self.report.append(line) for line in self.reader if line['employee_id'] == employee_id]
        return self.report, f'{employee_id} attendance report'

    def current_month_employees_attendance_report(self):
        """
        Prints all attendance entries for this month, from the log
        creates a list of lines for the report
        :return: the report, header
        """
        [self.report.append(line) for line in self.reader if
         datetime.datetime.strptime(line['date'], "%m/%d/%y").month == datetime.datetime.today().month]
        return self.report, 'Current month attendance report'

    def late_employees_attendance_report(self):
        """
        Prints all late entries (after 9:30) (for the previous month), from the log
        creates a list of lines for the report
        :return: the report, header
        """
        [self.report.append(line) for line in self.reader if
         datetime.datetime.strptime(line['time'], "%H:%M:%S").time() > datetime.time(9, 30, 0)]
        return self.report, 'Late attendance report'

    @staticmethod
    def print_report(func, loop1, loop2, par=None, header1=None, loop3=None, loop4=None):
        """
        prints reports in a friendly manner
        :param func: func
        :param loop1: str
        :param loop2: str
        :param par: str
        :param header1: str
        :param loop3: str
        :param loop4: str
        # :return:
        """
        if par:
            report, header = func(par)
        else:
            report, header = func()
        print(header)
        if header1:
            print(report[0][header1])
        for dic in report:
            print(f'{dic[loop1]} {dic[loop2]} ', end='')
            if loop3:
                print(f'{dic[loop3]} {dic[loop4]} ')
            else:
                print('')


chuck = employees_class.Employees('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv')
cory = Attendance('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv')
# print(cory.last_month_employees_attendance_report())
# print(cory.mark_attendance('1', chuck))
# Attendance.print_report(cory.employee_attendance_report, 'date', 'time', '1', 'name')
# cory.prnt(cory.current_month_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
# cory.late_employees_attendance_report()
Attendance.print_report(cory.late_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
