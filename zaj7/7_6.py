#(a) zwracający 0, 1, 0, 1, 0, 1, ...,
class InfiniteIterator:
    def __init__(self):
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current_value
        self.current_value = 1 - self.current_value
        return value


#(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
import random

class RandomDirectionIterator:
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)

random_direction_iterator = RandomDirectionIterator()


#(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
class WeekdayIterator:
    def __init__(self):
        self.current_day = 0

    def __iter__(self):
        return self

    def __next__(self):
        day = self.current_day
        self.current_day = (self.current_day + 1) % 7
        return day

weekday_iterator = WeekdayIterator()


#proste testy
# Sprawdzenie klasy InfiniteIterator

infinite_iterator = InfiniteIterator()
print("Infinite iterator:", end=" ")
for i in range(10):
    print(next(infinite_iterator), end=" ")

# Sprawdzenie klasy RandomDirectionIterator
random_direction_iterator = RandomDirectionIterator()
print("\nRandom directions:", end=" ")
for i in range(10):
    print(next(random_direction_iterator), end=" ")

# Sprawdzenie klasy WeekdayIterator
weekday_iterator = WeekdayIterator()
print("\nWeekday numbers:", end=" ")
for i in range(10):
    print(next(weekday_iterator), end=" ")