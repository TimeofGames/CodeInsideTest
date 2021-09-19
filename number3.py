class BuildingError(Exception):
    def __str__(self):
        return "BuildingError"


class FloorOutOfRange(BuildingError):
    def __str__(self):
        return "FloorOutOfRange"


class Building():
    def __init__(self, floors, lifts):
        self._floors = floors
        self._lifts = lifts
        self._lift_calls = []
        self._all_done = False

    @property
    def floors(self):
        return self._floors

    @floors.setter
    def floors(self, new_floors):
        self._floors = new_floors

    @property
    def lifts(self):
        return self._lifts

    @lifts.setter
    def lifts(self, new_lifts):
        self._lifts = new_lifts

    @property
    def all_done(self):
        return self._all_done

    def call_lift(self, floor, move_to):
        if floor <= self._floors:
            self._lift_calls.append([floor, move_to])
        else:
            raise FloorOutOfRange

    def _lift_controller(self):
        while len(self._free_lifts) != 0 and len(self._lift_calls) > 0:
            count = 0
            nearest = None
            smallest_distance = 9
            for i in self._free_lifts:
                if abs(i.floor - self._lift_calls[0][0]) <= smallest_distance and self._not_only_on_first_floor(i):
                    count += 1
                    nearest = i
                    smallest_distance = abs(i.floor - self._lift_calls[0][0])
            if nearest is not None:
                nearest.move_to = self._lift_calls.pop(0)
            elif count == 0:
                break

    def _not_only_on_first_floor(self, lift):
        count = 0
        if lift.floor != 1:
            return True
        else:
            for i in self._free_lifts:
                if i.floor == 1:
                    count += 1
            if count > 1:
                return True
            else:
                return False

    def _lifts_update(self):
        for i in self._lifts:
            if i.move_to is None:
                continue
            elif i.move_to != i.floor:
                i.move()
            else:
                continue

    @property
    def _free_lifts(self):
        free_lefts = []
        for i in self._lifts:
            if i.move_to is None:
                free_lefts.append(i)
        return free_lefts

    def _chech_end(self):
        if len(self._free_lifts) == 3 and len(self._lift_calls) == 0:
            self._all_done = True
        else:
            self._all_done = False


    def print_lifts(self):
        for i in self._lifts:
            print(i.floor, end=" ")
        print()

    def iteration(self):
        self._lift_controller()
        self._lifts_update()
        self.print_lifts()
        self._chech_end()


class Lift():
    def __init__(self):
        self._move_to = None
        self._floor = 1

    @property
    def move_to(self):
        return self._move_to

    @move_to.setter
    def move_to(self, new_move_to):
        self._move_to = new_move_to
        if self._move_to[0] == self._floor:
            self._move_to.pop(0)

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, new_floor):
        self._floor = new_floor

    def move(self):
        if len(self._move_to) == 2:
            self._floor = self._move_to.pop(0)
        elif len(self._move_to) == 1:
            self._floor = self._move_to.pop(0)
            self._move_to = None


lifts = []
for _ in range(3):
    lifts.append(Lift())
building = Building(9, lifts)
building.print_lifts()

while True:
    while True:
        call = input("Вызвать лифт? y/n ")
        if call == "y":
            call = input("Укажите откуда и куда через пробел ").split(" ")
            call = [int(i) for i in call]
            building.call_lift(call[0], call[1])
        else:
            break
    building.iteration()
    exit = input("Закрыть? y/n ")
    if exit == "y":
        while not building.all_done:
            building.iteration()
        break
