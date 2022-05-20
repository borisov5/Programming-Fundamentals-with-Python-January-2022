class Car:
    def __init__(self, name, mileage, available_fuel):
        self.name = name
        self.mileage = mileage
        self.available_fuel = available_fuel

    def __repr__(self):
        return self.name


cars = {}

number_of_cars = int(input())
for num in range(number_of_cars):
    info = input().split("|")
    car_name = info[0]
    car_mileage = info[1]
    car_fuel = info[2]
    cars[car_name] = Car(car_name, int(car_mileage), int(car_fuel))

command = input().split(" : ")
while command[0] != 'Stop':
    command_type = command[0]
    car_name = command[1]

    if command_type == 'Drive':
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car_name].available_fuel < fuel:
            print("Not enough fuel to make that ride")
        elif cars[car_name].available_fuel >= fuel:
            cars[car_name].mileage += distance
            cars[car_name].available_fuel -= fuel
            print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car_name].mileage >= 100000:
            removed_car = cars.pop(car_name)
            print(f"Time to sell the {removed_car}!")

    elif command_type == 'Refuel':
        fuel = int(command[2])
        if cars[car_name].available_fuel + fuel > 75:
            required_fuel = 75 - cars[car_name].available_fuel
        else:
            required_fuel = fuel
        cars[car_name].available_fuel += required_fuel
        refueled_car = cars[car_name]
        print(f"{refueled_car} refueled with {required_fuel} liters")

    elif command_type == 'Revert':
        kilometers = int(command[2])
        cars[car_name].mileage -= kilometers
        if cars[car_name].mileage < 10000:
            cars[car_name].mileage = 10000
        elif cars[car_name].mileage >= 10000:
            print(f"{cars[car_name]} mileage decreased by {kilometers} kilometers")
    command = input().split(" : ")

sorted_cars = sorted(cars.values(), key=lambda c: (-c.mileage, c.name))
for car in sorted_cars:
    print(f"{car.name} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.available_fuel} lt.")
