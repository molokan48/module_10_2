import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self , name = str , power = int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        Enemy = 100
        day = 0
        print(f'{self.name}, на нас напали!!!')
        while Enemy > 0:
            sleep(1) ; day +=1 ; Enemy -= self.power
            print(f'{self.name} сражается {day} дней(дня) , осталось {Enemy} врагов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!!!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")