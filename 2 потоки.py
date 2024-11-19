import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 0



    def fight(self, name, power):
        bot = 100
        while bot > 0:
            time.sleep(1)
            self.day += 1
            bot -= self.power
            print(f"{self.name} сражается {self.day}..., осталось {bot} воинов.")




    def run(self):
        print(f"{self.name}, на нас напали!")

        self.fight(self.name, self.power)
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()

second_knight.start()


first_knight.join()

second_knight.join()

print("Все битвы закончены!!!")

# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения