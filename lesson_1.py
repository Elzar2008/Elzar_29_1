class Transport:
    def __init__(self, the_model, the_color, the_year):
        self.model = the_model
        self.color = the_color
        self.year = the_year

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_color, the_year):
        super().__init__(the_model, the_color, the_year)


class Car(Transport):
    wheels_number = 4
    counter = 0

    def __init__(self, the_model, the_color, the_year, penalties=0):
        super().__init__(the_model, the_color, the_year)
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    def __init__(self, the_model, the_color, the_year,
                 penalties=0, load_capacity=0):
        super().__init__(the_model, the_color, the_year, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} ({weight} kg) was successfully '
                  f'loaded to {self.model}')


print(f'We need {Car.wheels_number * 10 * 5000} soms for summer lastics.')

bmw_car = Car('BMW X7', 'Red', 2020)
print(bmw_car)
print(f'Model: {bmw_car.model} Color: {bmw_car.color} Year: {bmw_car.year} '
      f'Penalties: {bmw_car.penalties}')

honda_car = Car(the_color='Silver', the_model='Honda Civic', the_year=2009,
                penalties=1900)
print(f'Model: {honda_car.model} Color: {honda_car.color} Year: {honda_car.year} '
      f'Penalties: {honda_car.penalties}')

# bmw_car.color = 'Black'
bmw_car.change_color('Black')
print(f'Model: {bmw_car.model} New Color: {bmw_car.color} Year: {bmw_car.year} '
      f'Penalties: {bmw_car.penalties}')

bmw_car.drive('Osh')
honda_car.drive('Tokmok')

print(f'Was produced {Car.counter} cars.')

man_truck = Truck('Man 556', 'Blue', 2019, 0, 30000)

print(f'Model: {man_truck.model} Color: {man_truck.color} Year: {man_truck.year} '
      f'Penalties: {man_truck.penalties} Load capacity: {man_truck.load_capacity}')
man_truck.load_cargo('Apples', 35000)
man_truck.load_cargo('Potatoes', 25500)
man_truck.drive('Batken')

boeing_plane = Plane('Boeing 747', 'White', 2022)
print(f'Model: {boeing_plane.model} Color: {boeing_plane.color} '
      f'Year: {boeing_plane.year}')
