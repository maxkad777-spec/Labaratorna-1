class Car:
    def __init__(self, brand, model, year, number):
        self.brand = brand
        self.model = model
        self.year = year
        self.number = number
        self.is_repaired = True

    def get_info(self):
        return f"{self.brand} {self.model}, {self.year}, {self.number}"


class Owner:
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)


class Mechanic:
    def __init__(self, name, specialization, experience):
        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.orders = []

    def take_order(self, order):
        self.orders.append(order)
        order.status = "В роботі"

    def finish_order(self, order):
        order.status = "Завершено"
        order.car.is_repaired = True


class RepairOrder:
    def __init__(self, car, owner, problem, price):
        self.car = car
        self.owner = owner
        self.problem = problem
        self.price = price
        self.status = "Створено"

    def get_info(self):
        return f"{self.car.brand}: {self.problem}, {self.price} грн, {self.status}"


class ServiceStation:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.mechanics = []
        self.orders = []

    def add_mechanic(self, mechanic):
        self.mechanics.append(mechanic)

    def add_order(self, order):
        self.orders.append(order)
        order.car.is_repaired = False
owner = Owner("Іван", "0971234567", 30)

car = Car("Toyota", "Camry", 2018, "AB1234CD")
owner.add_car(car)

mechanic = Mechanic("Олег", "Двигуни", 7)

order = RepairOrder(
    car,
    owner,
    "Проблема з двигуном",
    4500
)

service = ServiceStation(
    "AutoFix",
    "м. Вінниця"
)

service.add_mechanic(mechanic)
service.add_order(order)

mechanic.take_order(order)

print(order.get_info())

mechanic.finish_order(order)

print(order.get_info())
