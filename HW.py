class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f'{self.name} РЅР°С‡Р°Р»Р° РґРІРёР¶РµРЅРёРµ'

    def stop(self):
        return f'{self.name} РѕСЃС‚РѕРЅР°РІРёР»Р°СЃСЊ'

    def turn_right(self):
        return f'{self.name} РїРѕРІРµСЂРЅСѓР»Р° РІРїСЂР°РІРѕ'

    def turn_left(self):
        return f'{self.name} РїРѕРІРµСЂРЅСѓР»Р° РІР»РµРІРѕ'

    def show_speed(self):
        return f'РЎРєРѕСЂРѕСЃС‚СЊ {self.name}: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'РЎРєРѕСЂРѕСЃС‚СЊ {self.name} : {self.speed}')

        if self.speed > 40:
            return f'РЎРєРѕСЂРѕСЃС‚СЊ {self.name} РїСЂРµРІС‹С€РµРЅР°'
        else:
            return f'РЎРєРѕСЂРѕСЃС‚СЊ {self.name} РЅРµ РїСЂРµРІС‹С€РµРЅР°'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'РЎРєРѕСЂРѕСЃС‚СЊ  {self.name}: {self.speed}')

        if self.speed > 60:
            return f'РЎРєРѕСЂРѕСЃС‚СЊ {self.name} РїСЂРµРІС‹С€РµРЅР°'


bmw = SportCar(200, 'Р‘РµР»Р°СЏ', 'BMW')
renault = TownCar(40, 'Р§РµСЂРЅС‹Р№', 'Renault')
lada = WorkCar(80, 'РљРѕСЂРёС‡РЅРµРІР°СЏ', 'Lada')
print(f'{bmw.name} {bmw.color}')
print(f'{renault.name} {renault.color}')
print(f'{lada.name} {lada.color}')
print(lada.turn_left())
print(f'{renault.turn_right()}, {bmw.stop()} ')
print(f'{lada.go()}, {lada.show_speed()}')
print(bmw.show_speed())
print(renault.show_speed())