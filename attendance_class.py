import datetime
import csv
import employees_class
import file


def singleton(my_class):
    instances = {}

    def get_instance(*args, **kwargs):
        if my_class not in instances:
            instances[my_class] = my_class(*args, **kwargs)
        return instances[my_class]

    return get_instance

@singleton
class Single(object):
pass

class SingleAttendance(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(SingleAttendance, self).__new__(self)
        return self._instance


class Attendance:
    __instance = None

    @staticmethod
    def get_instance():
        if Attendance.__instance is None:
            Attendance()
        return Attendance.__instance

    # todo anna- (why do i need also init?) (why do i need the exception? so i dont create twice)
    #  am i not allowed to start an instance the regular way? or why do i need getinstance? need explanations.
    #  should i use the __new__ or decorator?
    def __init__(self, address):
        if Attendance.__instance is not None:
            raise Exception('this class is a singleton')
        else:
            Attendance.__instance = self
            self.address = address

            # where will this be if no class? separate func i will run in each func? in main before each function?
            #  something more general?
            #  right now it doesnt update between func to func
            #  therefore it needs to be out of init and run separately in every func.
            try:
                with open(self.address) as f:
                    self.reader = list(csv.DictReader(f))
            except FileNotFoundError:
                self.reader = []

    # fieldnames = ['date', 'time', 'employee_id', 'name']

    #      check if file exists? should i assert an error and crash the program? or use the programs error
    #  if i need employee only in one function, i wont add it in init but in the function.
    # def __init__(self, address):
    #     """
    #     Will initiate the address to the object
    #     creates a list of reader which will be empty if the file doesnt exist yet
    #     :param address: str
    #     """
    #     self.address = address
    #
    #
    #     try:
    #         with open(self.address) as f:
    #             self.reader = list(csv.DictReader(f))
    #     except FileNotFoundError:
    #         self.reader = []

    def mark_attendance(self, employee_id, employee):
        """
        given an employee id, writes an attendance log to the attendance file
        Will check the employees_file for the employee_id. (and will take the name).
        if the file exists, will change write mode to append
        Will write date, time, id and name entry to the attendance log.
        :param employee_id: str
        :param employee: Employees
        :return: print
        """
        name = employee.search_employee([employee_id], True)
        if not name:
            return print(f'{employee_id} {employees_class.Employees.not_exist}')

        mode = 'w'
        if self.reader:
            mode = 'a'
        # date = datetime.date.today()
        # datetime.date(1992, 3, 12)
        time = datetime.datetime.now().strftime("%X")
        date = datetime.datetime.now().strftime("%x")
        param = [{'date': date, 'time': time, 'employee_id': employee_id, 'name': name}]
        fieldnames = ['date', 'time', 'employee_id', 'name']
        file.write_file(param, self.address, fieldnames, mode)

    def employee_attendance_report(self, employee_id):
        """
        Given an employee id, will return all its attendance entries.
        creates a list of lines for the report.
        prints a header.
        runs print function
        :param employee_id: str
        """
        report = []
        [report.append(line) for line in self.reader if line['employee_id'] == employee_id]
        print(f'{employee_id} {report[0]["name"]} Attendance Report')
        self._print(report)

    def current_month_attendance_report(self):
        """
        Prints all attendance entries for this month, from the log
        creates a list of lines for the report
        prints a header.
        runs print function
        """
        report = []
        [report.append(line) for line in self.reader if
         datetime.datetime.strptime(line['date'], "%m/%d/%y").month == datetime.datetime.today().month]
        print('Current Month Attendance Report\n')
        # print(f"{' '.join(Attendance.fieldnames).title()}\n")
        self._print(report, True)

    def late_attendance_report(self):
        """
        Prints all late entries (after 9:30) (for the previous month), from the log
        creates a list of lines for the report
        prints a header.
        runs print function
        """
        report = []
        [report.append(line) for line in self.reader if
         datetime.datetime.strptime(line['time'], "%H:%M:%S").time() > datetime.time(9, 30, 0)]
        print('Late Attendance Report\n')
        self._print(report, True)

    #
    def date_range_attendance_report(self, until, _from):
        report = []
        for line in self.reader:
            date = datetime.datetime.strptime(line['date'], "%m/%d/%y")
            if date > until:
                break
            #  how do i make him ask only until the answer is yes and then stop asking this question?
            if date >= _from:
                report.append(line)
                # while datetime.datetime(year1, month1, day1) <= datetime.datetime.strptime(line['date'], "%m/%d/%y") <=\
                #         datetime.datetime(year2, month2, day2):
                report.append(line)
        print(f'{_from.date()} - {until.date()} Attendance Report\n')
        self._print(report, True)

    def level_attendance_report(self, levels):
        #      i can make a set and have the for run once and check each time if its in the set

        ids = search(levels)
        report = []
        [report.append(line) for line in self.reader if line['employee_id'] in ids]
        print(f'{employee_id} {report[0]["name"]} Attendance Report')
        self._print(report)

    @staticmethod
    def _print(report, full=None):
        """
        prints reports in a friendly manner
        :param report: list
        :param full: boolean
        """
        for dic in report:
            print(f'{dic["date"]} {dic["time"]} ', end='')
            if full:
                print(f'{dic["employee_id"]} {dic["name"]} ')
            else:
                print('')


att = SingleAttendance()
att = SingleAttendance.get_instance()

chuck = employees_class.Employees('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv')
cory = Attendance('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv')
# until = datetime.datetime(2021, 1, 17)
# _from = datetime.datetime(2021, 1, 7)
# cory.date_range_attendance_report(until, _from)

# print(cory.last_month_employees_attendance_report())
# cory.mark_attendance('1', chuck)
print(cory.reader)
# cory.mark_attendance('1', chuck)
# print(cory.reader)
# Attendance.prnt(cory.employee_attendance_report, 'date', 'time', '1', 'name')
# cory.prnt(cory.current_month_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
# cory.late_employees_attendance_report()
# Attendance.prnt(cory.late_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
cory.employee_attendance_report('1')
# cory.current_month_attendance_report()
# cory.late_attendance_report()
