class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print("Elevator is now on floor", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print("Elevator is now on floor", self.current_floor)

    def go_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            return
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print("\nRunning elevator", elevator_number)
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFire alarm! Moving all elevators to the bottom floor.")
        for i in range(len(self.elevators)):
            self.run_elevator(i + 1, self.bottom_floor)

my_building = Building(1, 10, 3)
my_building.run_elevator(1, 5)
my_building.run_elevator(2, 7)
my_building.fire_alarm()