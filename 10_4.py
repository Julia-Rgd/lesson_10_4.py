from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables
        self.queue = Queue()
    def is_vacant(self):
        return not any(t.guest for t in self.tables)
    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            look_vacant_table = False
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} села за стол номер {table.number}")
                    look_vacant_table = True
                    break
            if not look_vacant_table:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            look_vacant_table = False
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} села за стол номер {table.number}")
                    look_vacant_table = True
                    break
            if not look_vacant_table:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not (self.queue.empty() and self.is_vacant()):
            for table in self.tables:
                if not table.guest:
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f"{table.guest.name} вышла из очереди и села за стол номер {table.number}")
                        table.guest.start()
                else:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал и ушел")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


"C:\Users\User\PycharmProjects\HELLO WORLD\.venv\Scripts\python.exe" "C:\Users\User\PycharmProjects\HELLO WORLD\module_10_4.py" 
Maria села за стол номер 1
Oleg села за стол номер 2
Vakhtang села за стол номер 3
Sergey села за стол номер 4
Darya села за стол номер 5
Arman в очереди
Vitoria в очереди
Nikita в очереди
Galina в очереди
Pavel в очереди
Ilya в очереди
Alexandra в очереди
Vakhtang покушал и ушел
Стол номер 3 свободен
Sergey покушал и ушел
Стол номер 4 свободен
Arman вышла из очереди и села за стол номер 3
Vitoria вышла из очереди и села за стол номер 4
Maria покушал и ушел
Стол номер 1 свободен
Nikita вышла из очереди и села за стол номер 1
Darya покушал и ушел
Стол номер 5 свободен
Oleg покушал и ушел
Стол номер 2 свободен
Galina вышла из очереди и села за стол номер 5
Pavel вышла из очереди и села за стол номер 2
Arman покушал и ушел
Стол номер 3 свободен
Ilya вышла из очереди и села за стол номер 3
Nikita покушал и ушел
Стол номер 1 свободен
Alexandra вышла из очереди и села за стол номер 1
Vitoria покушал и ушел
Стол номер 4 свободен
Pavel покушал и ушел
Стол номер 2 свободен
Galina покушал и ушел
Стол номер 5 свободен
Ilya покушал и ушел
Стол номер 3 свободен
Alexandra покушал и ушел
Стол номер 1 свободен

Process finished with exit code 0
