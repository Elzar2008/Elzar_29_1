from enum import Enum


class Color(Enum):
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'


class Drawable:
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:

    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print(f'Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    # def __init__(self):
    #     pass
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError('Wrong data type')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if isinstance(value, Color):
            self.__color = value
        else:
            raise ValueError('Wrong data type')

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return f'Model: {self.__model} Year: {self.__year} ' \
               f'Color: {self.__color.value}{self.__color.name}\033[0m'

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year < other.__year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'Ai - 95'

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using electricity')

    def __str__(self):
        return super().__str__() + f' Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


print(f'FuelCar Fabric had: {FuelCar.get_total_fuel_amount()}')

# some_car = Car('Nissan Patrol', 2020)
# print(some_car)

bmw_car = FuelCar('BMW M5', 2009, Color.OKBLUE, 65)
print(bmw_car)

tesla_car = ElectricCar('Tesla Model S', 2022, Color.OKCYAN, 450)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2019, Color.OKGREEN, 45, 200)
print(toyota_car)
print(toyota_car.drive())

print(HybridCar.mro())

num_1 = 9
num_2 = 5
print(f'Num 1 is bigger than Num 2 {num_1 > num_2}')
print(f'Num 1 equals Num 2 {num_1 == num_2}')

print(f'Toyota is better than BMW {toyota_car > bmw_car}')
print(f'Total fuel amount: {toyota_car + bmw_car}')

tesla_car.play_music('Muras')

samsung_phone = SmartPhone()
samsung_phone.play_music('Kamarof')
samsung_phone.stop_music()

tesla_car.draw('🚗')
samsung_phone.draw('📱')

print(f'Fuel Car Fabric has: {FuelCar.get_total_fuel_amount()} '
      f'({FuelCar.get_fuel_type()})')

# FuelCar.__total_fuel_amount -= 100
# print(f'Fuel Car Fabric has: {FuelCar.get_total_fuel_amount()}')

if bmw_car.model == 'BWM M5':
    print('This car is cool')


if tesla_car.color == Color.OKCYAN:
    print('Tesla car is beautiful')