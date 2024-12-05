from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int, enem_num: int = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.enem_num = enem_num

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enem_num > 0:
            self.enem_num -= self.power
            days += 1
            print(f"{self.name} сражается {days}..., осталось {self.enem_num} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')