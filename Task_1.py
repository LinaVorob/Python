import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def running(self):
        for color in cycle(self.__color.keys()):
            print(color)
            time.sleep(self.__color[color])


traffic = TrafficLight()
traffic.running()
