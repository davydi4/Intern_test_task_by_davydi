class Entity(object):
    def __init__(self, cat):
        self.cat = cat

    def __str__(self):
        return f'Сущность: {self.cat}'


class Employee(object):
    def __init__(self, employee, company):
        self.employee = employee
        self.company = company

    def __str__(self):
        return f'{self.employee} работает в {self.company}'


if __name__ == '__main__':
    cat = Entity('Сугроб')
    print(cat)

    employee = Employee('Петя', 'Foxford')
    print(employee)
