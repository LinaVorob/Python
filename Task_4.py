class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = float(speed), color, name, is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}' if direction[:2] == 'на' else f'{self.name} повернула на{direction}'

    def show_speed(self):
        return f'Скорость автомобиля: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'ВНИМАНИЕ! ПРЕВЫШЕНИЕ СКОРОСТИ! Скорость автомобиля: {self.speed}'
        else:
            return f'Скорость автомобиля: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'ВНИМАНИЕ! ПРЕВЫШЕНИЕ СКОРОСТИ! Скорость автомобиля: {self.speed}'
        else:
            return f'Скорость автомобиля: {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


def control(position):
    print(position.go())
    print(f'{position.turn("налево")}, {town_car.turn("право")}')
    print(position.stop())
    print(position.show_speed())


police_car = PoliceCar(90, 'blue', 'BMW')
town_car = TownCar(120, 'red', 'LADA')
work_car = WorkCar(39, 'yellow', 'Toyota')
sport_car = SportCar(190, 'purple', 'Dodge')

print(f'{police_car.color} {police_car.name} have speed {police_car.speed}. Is it police car? {police_car.is_police}')
print(f'{town_car.color} {town_car.name} have speed {town_car.speed}. Is it police car? {town_car.is_police}')
print(f'{work_car.color} {work_car.name} have speed {work_car.speed}. Is it police car? {work_car.is_police}')
print(f'{sport_car.color} {sport_car.name} have speed {sport_car.speed}. Is it police car? {sport_car.is_police}')

control(police_car)
control(town_car)
control(work_car)
control(sport_car)
