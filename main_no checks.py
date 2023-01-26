from employees_class import *
from attendance_return import *

address_e = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Employees.csv'
address_a = 'C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\data\\Attendance log.csv'
employee = Employees(address_e)
attendance = Attendance(address_a, )

while True:
    function = input(
        '\nFor ENDING the program type 0.\n\nFor ADDING an employee manually type 1.\nFor ADDING from a file type 2.\n'
        'For DELETING an employee manually type 3.\nFor DELETING employees from a file type 4.\n'
        'For marking your ATTENDANCE type 5.\nFor generating an EMPLOYEE report type 6.\nFor generating last MONTHS '
        'attendance report type 7.\nFor generating LATE attendance report type 8. \n')
    if function == '0':
        break
    elif function == '1':
        employee.add_employee()

    elif function == '2':
        print(employees_class.check_address(employee.add_employees_from_file))

    elif function == '3':
        employee.delete_employee()

    elif function == '4':
        print(employee.delete_employees_from_file())


    # elif function == '5':
    #     mark_attendance(self, employee_id, employees_file)
    # elif function == '6':
    #     employee_attendance_report(self, employee_id)
    # elif function == '7':
    #     last_month_employees_attendance_report(self)
    # elif function == '8':
    #     last_month_late_employees_attendance_report(self)
    else:
        continue
    break

    # def add_employee(self):
    #     """
    #     Will add a new employee to the Employee file.
    #     #:return:
    #
    #     -open and write to the file with commas
    #     """
    #     employee_id = check_str('employee_id', str.isdigit, 'i')
    #     name = check_str('name', str.isalpha, '1')
    #     phone = check_str('phone', str.isdigit, 'i')
    #     age = check_str('age', str.isdigit, 'i')
    #     param = [{'employee_id': employee_id, 'name': name, 'phone': phone, 'age': age}]
    #     self.append_file(param)