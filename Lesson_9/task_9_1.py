from time import sleep
from itertools import cycle

class TrafficLight:
    __colors = ["красный", "желтый", "зеленый", "желтый"]

    def __init__(self, value1, value2, value3):
        # self.color_name = ['Красный', 'Желтый','Зеленый', 'Желтый']
        self.__color = self.__colors[0]
        self.value = [value1, value2, value3, value2]
        self.__iter_light = cycle(zip(self.__colors, self.value))

    def state(self):
        return self.__color


    def running(self):
        count = 0

        for key, value in cycle(self.__iter_light):
            if count > 6:
                break
            print(f"Зажегся {key} - Время: {value}s ")
            # print(key)
            sleep(value)
            count += 1



traf = TrafficLight(7, 2, 2)
traf.running()
traf.state()




#
# class TrafficLight:
#     def __init__(self, color):
#         self._color = color
#     def running(self):
#         for key, value in self._color.items():
#             sleep(value)
#             print(key)
#
#
# traf = TrafficLight(color={
#     "Красный": 7,
#     "Желтый": 2,
#     "Зеленый": 7})
# traf.running()