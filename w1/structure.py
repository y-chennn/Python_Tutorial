class cars():
    def __init__(self, brand, color) -> None:
        self.brand = brand
        self.color = color

    def drive():
        pass

    def reverse():
        pass

    def parking():
        pass

    def turn(dir):
        pass

def is_obstacle()->bool:
    pass

def can_turn_left()->bool:
    pass

def is_dest()->bool:
    pass

def main():
    car = cars()
    car.brand = 'toyota'
    car.color = 'yellow'

    while(is_dest() != True):
        car.drive()
        # condition: turn left?
        # condition: turn right?
        # condition: stop?
    car.parking()   


if __name__ == '__main__':
    main()