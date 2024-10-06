import threading
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            z = randint(50, 500)
            self.balance += z
            print(f'Пополнение:{z}. Баланс:{self.balance}' + '\n')
            sleep(0.001)

    def take(self):
        for i in range(100):
            x = randint(50, 500)
            print(f'Запрос на {x}' + '\n')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}.' + '\n')
            else:
                print(f'Запрос отклонен, недостаточно средств' + '\n')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')