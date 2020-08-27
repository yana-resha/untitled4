from application.salary import calculate_salary
from db.people import get_employees
from datetime import datetime, date, time

print(datetime.now())

if __name__ == '__main__':
    print(calculate_salary(12))
    print(get_employees(2))