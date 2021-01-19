class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return float(self._income["wage"]) + float(self._income["bonus"])
        except ValueError:
            return None


worker_first = Position('Лина', 'Воробьева', 'инженер-конструктор', 30000, 12000)
worker_second = Position('Максим', 'Иванов', 'технолог', 27000, 15000)
worker_third = Position('Алена', 'Крива', 'нормировщик', 35000, 20000)

print(worker_first.name)
print(worker_second.position)

print(f'Доход сотрудника {worker_first.get_full_name()}: {worker_first.get_total_income()}')
print(f'Доход сотрудника {worker_second.get_full_name()}: {worker_second.get_total_income()}')
print(f'Доход сотрудника {worker_third.get_full_name()}: {worker_third.get_total_income()}')
