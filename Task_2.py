class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self, weight, sm):
        print(
            f'Масса асфальта для покрытия дороги {self._length}м х {self._width}м:'
            f' {(self._width * self._length * weight * sm) / 1000:.2f}т.')


road = Road(5000, 20)
road.mass_asphalt(25, 5)
