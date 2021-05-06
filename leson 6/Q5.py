from Q4 import TownCar, SportCar, WorkCar, PoliceCar

if __name__ == '__main__':
    town_car = TownCar('Yellow', 'Mazda CX-5')
    sport_car = SportCar('Red', 'Ferrari F40')
    work_car = WorkCar('White', 'Ford Mondeo')
    police_car = PoliceCar('Blue', 'Toyota Camry')

    town_car.go(80)
    print(f"{town_car.color} {town_car.name} едет со скоростью {town_car.speed}")
    sport_car.go(260)
    print(f"{sport_car.color} {sport_car.name} разогналась до скорости {sport_car.speed}")
    police_car.go(220)
    print(
        f"{police_car.name} не остановила {sport_car.name}, т.к. не смогла разогнаться выше {police_car.speed}")
    work_car.go(100)
    print(f"{police_car.name} остановила {work_car.name}, двигавшуюся со скоростью {work_car.speed}")
