import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} Status ---")
        print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Cur Speed':<10} | {'Distance':<10}")
        print("-" * 47)
        for car in self.car_list:
            print(f"{car.registration_number:<10} | {car.maximum_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return False

cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not derby.race_finished():
    derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nHour: {hours}")
        derby.print_status()

print(f"\nRace Finished at hour: {hours}")
derby.print_status()