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
owner1 = Owner(
    "Іван Петренко",
    "0971234567",
    30
)

owner2 = Owner(
    "Марія Коваль",
    "0639876543",
    27
)

car1 = Car(
    "Toyota",
    "Camry",
    2018,
    "AB1234CD"
)

car2 = Car(
    "BMW",
    "X5",
    2020,
    "AA5555BB"
)

car3 = Car(
    "Volkswagen",
    "Passat",
    2017,
    "AI7777KT"
)

owner1.add_car(car1)
owner1.add_car(car2)
owner2.add_car(car3)


mechanic1 = Mechanic(
    "Олег",
    "Двигуни",
    7
)

mechanic2 = Mechanic(
    "Андрій",
    "Ходова частина",
    5
)

mechanic3 = Mechanic(
    "Сергій",
    "Електрика",
    10
)

service = ServiceStation(
    "AutoFix",
    "м. Вінниця"
)

service.add_mechanic(mechanic1)
service.add_mechanic(mechanic2)
service.add_mechanic(mechanic3)
service.add_order(order)

mechanic.take_order(order)

print(order.get_info())

mechanic.finish_order(order)

print(order.get_info())
