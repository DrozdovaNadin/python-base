# Реализуйте класс Car (машина)

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        self.s = self.speed * 1.2
        return f'{self.name} тронулась, скорость была {self.speed}, стала скорость {self.s}'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f"{self.name} повернула " + direction

    def show_speed(self):
        return f'Текущая скорость {self.name}  {self.speed}'


class TownCar(Car):
    speed_stp = 60
    def __init__(self, speed, color, name, is_police ):
        super().__init__(speed, color, name, is_police)
        # self.speed_stp = 60

    def show_speed(self):
        print(f'Текущая скорость машины {self.name}  {self.speed}')

        if self.speed > self.speed_stp:
            return f'Скорость {self.name} выше чем разрешенная'
        else:
            return f'Скорость {self.name} нормальная'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    speed_stp = 40
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name}  {self.speed}')

        if self.speed > self.speed_stp:
            return f'Скорость {self.name} выше разрешенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(70, 'White', 'Oka', False)
lada = WorkCar(50, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn('Налево'))
print(f'Когда {oka.turn("направо")}, тогда {audi.stop()}')
print(f'{lada.go()} , {lada.show_speed()}')
print(f'Эта {audi.name} из полиции? {audi.is_police}')
print(f'Эта {lada.name}  из полиции? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())