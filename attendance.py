import datetime
import employees
import file

#     TODO check if file exists? should i assert an error and crash the program? or use the programs error
# TODO if i need employee only in one function, i wont add it in init but in the function.
ADDRESS = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv'
date_time = datetime.datetime.strptime
FIELDNAMES = ['Date', 'Time', 'Employee ID', 'Name', 'Level']


# todo- where will this be if no class? separate func i will run in each func? in main before each function?
#  something more general?
#  right now it doesnt update between func to func
#  therefore it needs to be out of init and run separately in every func.
#  reader- if this were a class i would create a reader in init, and run it again after each mark.
#       and then i wouldnt run it in each report.

# todo test- check returns.
#  -check write to file
def mark_attendance(employee_id):
    """
    given an employee id, writes an attendance log to the attendance file.
    Will check the employees file for the employee_id. (and will take the name).
    if the attendance file exists, will change write mode to append.
    Will write date, time, id and name entry (and level if applicable) to the attendance log.
    :param employee_id: str
    :return: print
    """
    employee_info = employees.search_employee(set(employee_id), employees.FIELDNAMES[0], 'name')
    if employee_info == employees.NOT_EXIST:
        return print(employee_info)
    name, level = employee_info

    mode = 'w'
    # todo- do i need to write module.func?
    if file.get_reader(ADDRESS):
        mode = 'a'

    now = datetime.datetime.now().strftime

    line = [{FIELDNAMES[0]: now("%x"), FIELDNAMES[1]: now("%X"), FIELDNAMES[2]: employee_id, FIELDNAMES[3]: name,
             FIELDNAMES[4]: level}]
    file.write_file(line, ADDRESS, FIELDNAMES, mode)


# todo test- check runs when empty
def employee_attendance_report(employee_id, comb=None):
    """
    Given an employee id, will return all its attendance entries.
    creates a list of lines for the report.
    prints a header.
    runs print function
    :param employee_id: str
    :param comb: str
    """
    # todo- if i had a class, i would run get reader, and update the reader attribute, at the end of mark.
    #  (cause the reader changed). if it can change, out of the control of the function needing it,
    #  maybe its better not to have it as an attribute
    reader = file.get_reader(ADDRESS)
    report = [line for line in reader if line[FIELDNAMES[2]] == employee_id]


    try:
        # will this try work?
        return _report(f'{employee_id} {report[0][FIELDNAMES[3]]}', report, comb)
    except IndexError:
        print('Empty report')

    try:
        header = f'{employee_id} {report[0][FIELDNAMES[3]]}'
        if comb:
            return report, header
        _print(report, header)
    except IndexError:
        print('Empty report')


def _report(header, report, comb=None, full=None):
    if comb:
        return report, header
    _print(report, header, full)



# todo test- check runs when empty.
#  - check report is right
def current_month_attendance_report(comb=None):
    """
    Prints all attendance entries for this month, from the log
    creates a list of lines for the report
    prints a header.
    runs print function
    :param comb: str
    """
    # todo if i want to do previous month, then i do minus 1 to month unless 1 and then 12 and minus 1 to year.
    reader = file.get_reader(ADDRESS)
    today = datetime.datetime.today()

    report = [line for line in reader if date_time(line[FIELDNAMES[0]], "%m/%d/%y").month == today.month and
              date_time([FIELDNAMES[0]], "%m/%d/%y").year == today.year]

    return _report('Current Month', report, comb, True)


# todo test- check runs when empty
def late_attendance_report(comb=None):
    """
    Prints all late entries (after 9:30) from the log
    creates a list of lines for the report
    prints a header.
    runs print function
    :param comb: str
    """
    reader = file.get_reader(ADDRESS)
    report = [line for line in reader if date_time(line[FIELDNAMES[1]], "%H:%M:%S").time() > datetime.time(9, 30, 0)]

    return _report('Late', report, comb, True)


# combine with level, employee, late
# todo test- check runs when empty.
#  -check different dates.
#  - check report works.
def date_range_attendance_report(until, _from, comb=None):
    """
    Prints all entries from a date range, from the log
    creates a list of lines for the report
    prints a header.
    runs print function
    @param until: date
    @param _from: date
    :param comb: str
    """
    reader = file.get_reader(ADDRESS)
    report = []
    for line in reader:
        date = date_time(line[FIELDNAMES[0]], "%m/%d/%y")

        # # TODO anna how do i make him ask only until the answer is yes and then stop asking this question?
        # #  i can do the same as current month. is the while better than if or the same?

        if date >= _from:
            if date > until:
                break
            report.append(line)

    return _report(f'{_from} - {until}', report, comb, True)

    # todo anna- which version is better?
    reader = iter(file.get_reader(ADDRESS))
    while True:
        try:
            line = next(reader)
        except StopIteration:
            break
        # todo anna- is this version different technically to the one above? think not. is it the same as for if?
        while datetime.datetime(year1, month1, day1) <= date_time(line['date'], "%m/%d/%y") <= \
                datetime.datetime(year2, month2, day2):
            report.append(line)
            try:
                line = next(reader)
            except StopIteration:
                break
        if report:
            break


# todo test- check runs when empty.
#  -check report works.
def level_attendance_report(levels, comb=None):
    """
 Prints attendance by position level, from the log
    creates a list of lines for the report
    prints a header.
    runs print function
    @param levels:list
    :param comb: str
    """
    reader = file.get_reader(ADDRESS)
    report = [line for line in reader if line[FIELDNAMES[4]] in levels]

    return _report(f"{','.join(levels)}", report, comb, True)


# old version. if there is no level in attendance log
def level_attendance_reportold(levels):
    reader = file.get_reader(ADDRESS)
    ids = employees.search_employees(levels, 1)
    report = [line for line in reader if line['employee_id'] in ids]
    print(f'{levels} Attendance Report')
    _print(report, str)


#     todo-
#      i can make a set and have the for run once and check each time if its in the set.
#       make sure the profile works when the report is empty (?)

# todo anna- how is best to intersect the lists? (reports). i can convert one (or 2) into a set for the in
#  explain this- your way (set(frozenset(items()))didnt save the order.
#  doesnt work for me- items wont work on list. set wont work on ordered dic
#  (i can have 2 loops for 01 and for 02 and a third combining them. that will always work.)
#  something didnt work with the indices, not sure what.
#  do i need list=[[][][]] and put in the right index? not sure what i wanted to do here.* maybe for header extend
#  header from original functions as well?
#  i can make an intersect and in a for go over shortest list and check if its in the intersect. unnecessary?
#  anna is this way the best way?
#  For word in set:
# 		List.count(word)
def combination_attendance_report(reports, header):
    """
    prints an intersection of up to 3 reports
    @param reports: list
    @param header: list
    """
    report = []
    if len(reports) <= 2:
        for line in reports[0]:
            if line in reports[1]:
                report.append(line)
    else:
        for line in reports[0]:
            if line in reports[1] and line in reports[2]:
                report.append(line)

    _report(f"{' '.join(header)}", report, True)


# todo check no level prints right. maybe no need to separate cause looks the same
def _print(report, header, full=None):
    """
    prints reports in a friendly manner
    :param header: str
    :param report: list
    :param full: boolean
    """
    print(header + 'Attendance Report\n')

    for dic in report:
        print(f'{dic[FIELDNAMES[0]]} {dic[FIELDNAMES[1]]} ', end='')
        if full and dic[FIELDNAMES[4]]:
            print(f'{dic[FIELDNAMES[2]]} {dic[FIELDNAMES[3]]} {dic[FIELDNAMES[4]]}')
        elif full:
            print(f'{dic[FIELDNAMES[2]]} {dic[FIELDNAMES[3]]} ')
        # need?
        else:
            print('')


# chuck = employees_class.Employees('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv')
# cory = Attendance('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv')
# until = datetime.datetime(2021, 1, 17)
# _from = datetime.datetime(2021, 1, 7)
# cory.date_range_attendance_report(until, _from)

# print(cory.last_month_employees_attendance_report())
# cory.mark_attendance('1', chuck)
# print(cory.reader)
# cory.mark_attendance('1', chuck)
# print(cory.reader)
# Attendance.prnt(cory.employee_attendance_report, 'date', 'time', '1', 'name')
# cory.prnt(cory.current_month_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
# cory.late_employees_attendance_report()
# Attendance.prnt(cory.late_employees_attendance_report, 'date', 'time', loop3='employee_id', loop4='name')
# cory.employee_attendance_report('1')
# cory.current_month_attendance_report()
# cory.late_attendance_report()
# employee_attendance_report('1')
