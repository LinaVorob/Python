class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'С помощью ручки {self.title} удобно рисовать калиграфию')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Карандаш {self.title} акварельный. Его лучше использовать для морских пейзажей')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Маркер {self.title} подходит для школьной доски')


pen = Pen('Parker')
pencil = Pencil('Derwent')
handle = Handle('Marker')

pen.draw()
pencil.draw()
handle.draw()
