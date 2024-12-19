import threading
import time
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        enemy = 100
        while enemy != 0:
            time.sleep(1)
            day += 1
            enemy = enemy - self.power
            print(f'{self.name} сражается {day} день(дня), осталось {enemy} воинов')

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
