class Road:
    # __length = None
    # __width = None
    # weigth = None
    # tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def intake(self):
        self.weigth = 25
        self.tickness = 5
        intake = int(self.length * self.width * self.weigth * self.tickness /1000)

        print(f'{self.length} м*{self.width} м*{self.weigth} кг*{self.tickness} см = {intake} т')

# road_to_village = Road(10, 6000)
road_to_village = Road(20, 5000)
road_to_village.intake()