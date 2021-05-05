from Q4 import TownCar, SportCar, WorkCar, PoliceCar

if __name__ == '__main__':
    town_car = TownCar(name="Mazda CX-5", color="Red", speed=58, is_police=False)
    sport_car = SportCar(name="Ferrari F40", color="Yellow", speed=284, is_police=False)
    work_car = WorkCar(name="Ford Mondeo", color="White", speed=45, is_police=False)
    police_car = PoliceCar(name="Toyota Camry", color="Blue & White", speed=160, is_police=True)

    print(f"{town_car.color} {town_car.go()} со скоростью {town_car.show_speed()}")
    print(f"{sport_car.color} {sport_car.go()} со скоростью {sport_car.show_speed()}")
    print(
        f"{police_car.name} не остановила {sport_car.name}, т.к. не смогла разогнаться выше {police_car.show_speed()}")
    print(f"{police_car.name} остановила {work_car.name}, двигавшуюся со скоростью {work_car.show_speed()}")
