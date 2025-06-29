"""
Каждое задание включает:
- Подробное описание
- Начальные данные для входа
- Ожидаемый результат (тест)
"""


# Задание 1
# Создайте базовый класс Animal с атрибутом name и методом make_sound(), который возвращает строку "Животное издает звук".
# Создайте класс Dog, наследующий Animal, который переопределяет make_sound() и возвращает "Собака лает".
# Вход: Dog("Бобик")
# Тест: dog.make_sound() -> "Собака лает"

class Animal:
    def __init(self, name):
        self.name = name

    def make_sound(self):
        return "Животное издает звук"

class Dog(Animal):

    def make_sound(self):
        print("Собака лает")


dog= Dog()
dog.make_sound()


# Задание 2
# Создайте класс Person с атрибутами name и age, а также методом introduce().
# Подкласс Student должен добавлять атрибут university и переопределять introduce(), добавляя университет.
# Вход: Student("Иван", 20, "МГУ")
# Тест: student.introduce() -> "Меня зовут Иван, мне 20 лет, я учусь в МГУ"

class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def introduce(self):
        pass

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет, я учусь в {self.university}")


student = Student("Иван", 29, "МГУ")
student.introduce()

# Задание 3
# Создайте класс Vehicle с атрибутом speed и методом move().
# Класс Car наследует Vehicle и добавляет атрибут brand. Переопределите move() с выводом: "Машина {brand} едет со скоростью {speed} км/ч".
# Вход: Car(120, "Toyota")
# Тест: car.move() -> "Машина Toyota едет со скоростью 120 км/ч"

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        print(f"Машина {self.brand} едет со скоростью {self.speed} км/ч")


car = Car(120, "Toyota")
car.move()


# Задание 4
# Создайте класс Shape с методом area(), возвращающим 0.
# Создайте подкласс Rectangle с атрибутами width и height и переопределите метод area(), чтобы он возвращал площадь.
# Вход: Rectangle(5, 4)
# Тест: rect.area() -> 20

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

rec = Rectangle(5, 4)
rec.area()


# Задание 5
# Создайте базовый класс Employee с атрибутом name и методом work(), возвращающим "Работник работает".
# Подкласс Manager переопределяет work() и возвращает "Менеджер управляет проектами".
# Вход: Manager("Анна")
# Тест: mgr.work() -> "Менеджер управляет проектами"

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print(f"Менеджер управляет проектами")

mgr = Manager("Анна")
mgr.work()

# Задание 6
# Создайте класс Appliance с методом turn_on(), возвращающим "Прибор включен".
# Подкласс WashingMachine должен переопределить turn_on() и возвращать "Стиральная машина начала стирку".
# Вход: WashingMachine()
# Тест: wm.turn_on() -> "Стиральная машина начала стирку"

class Appliance:
    def turn_on(self):
        return "Прибор включен"

class WashingMachine(Appliance):
    def turn_on(self):
        print("Стиральная машина начала стирку")


wm = WashingMachine()
wm.turn_on()


# Задание 7
# Создайте класс Book с атрибутом title и методом info().
# Подкласс Ebook должен добавлять атрибут file_size и переопределять info(), включая размер файла.
# Вход: Ebook("Python 101", 5)
# Тест: ebook.info() -> "Книга: Python 101, размер файла: 5MB"

class Book:
    def __init__(self, title):
        self.title = title

    def info(self):
        pass

class Ebook(Book):
    def __init__(self,title, file_size):
        super().__init__(title)
        self.file_size = file_size

    def info(self):
        print(f"Книга: {self.title}, размер файла: {self.file_size}")

ebook = Ebook("Python 101", 5)
ebook.info()


# Задание 8
# Создайте класс Shape с методом draw(), который возвращает "Рисуем фигуру".
# Подкласс Circle должен переопределять draw() и возвращать "Рисуем круг".
# Вход: Circle()
# Тест: c.draw() -> "Рисуем круг"

class Shape:
    def draw(self):
        return "Рисуем фигуру"

class Circle(Shape):
    def draw(self):
        print("Рисуем круг")

c = Circle()
c.draw()


# Задание 9
# Создайте класс Animal с методом eat(), возвращающим "Животное ест".
# Подкласс Cat переопределяет eat() и возвращает "Кот ест рыбу".
# Вход: Cat()
# Тест: cat.eat() -> "Кот ест рыбу"

class Animal:
    def eat(self):
        return "Животное ест"

class Cat(Animal):
    def eat(self):
        print("Кот ест рыбу")

cat = Cat()
cat.eat()

# Задание 10
# Создайте класс BankAccount с атрибутом balance.
# Подкласс SavingsAccount добавляет атрибут interest_rate и метод add_interest(), который увеличивает баланс.
# Вход: SavingsAccount(1000, 0.05)
# Тест: после add_interest() баланс = 1050

class BankAccount:
    def __init__(self, balance):
        self.balance = balance


class SavingAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        self.balance += self.balance * self.interest_rate


account = SavingAccount(1000, 0.05)
account.add_interest()
print(account.balance)
        


# Задание 11
# Создайте класс Animal с атрибутом species.
# Подкласс Bird добавляет метод fly(), который возвращает "Птица летит".
# Вход: Bird("Орёл")
# Тест: b.fly() -> "Птица летит"

# Задание 12
# Создайте класс Employee с методом work().
# Подкласс Developer переопределяет work(), возвращая "Разрабатывает программное обеспечение".
# Вход: Developer()
# Тест: dev.work() -> "Разрабатывает программное обеспечение"

# Задание 13
# Создайте класс Computer с атрибутом os.
# Подкласс Laptop добавляет атрибут weight и метод details().
# Вход: Laptop("Windows", 1.5)
# Тест: laptop.details() -> "Ноутбук с ОС Windows весит 1.5 кг"

# Задание 14
# Создайте класс Shape с методом perimeter(), возвращающим 0.
# Подкласс Square с атрибутом side переопределяет perimeter() для вычисления периметра.
# Вход: Square(4)
# Тест: square.perimeter() -> 16

# Задание 15
# Создайте класс Instrument с методом play(), возвращающим "Играем на инструменте".
# Подкласс Guitar переопределяет play(), возвращая "Играем на гитаре".
# Вход: Guitar()
# Тест: g.play() -> "Играем на гитаре"

# Задание 16
# Создайте класс Vehicle с методом stop(), возвращающим "Транспорт остановился".
# Подкласс Bus должен переопределить stop() и возвращать "Автобус остановился на остановке".
# Вход: Bus()
# Тест: bus.stop() -> "Автобус остановился на остановке"

# Задание 17
# Создайте класс User с атрибутом username.
# Подкласс Admin должен добавлять метод ban_user(), возвращающий "Пользователь заблокирован".
# Вход: Admin("root")
# Тест: admin.ban_user() -> "Пользователь заблокирован"

# Задание 18
# Создайте класс Media с методом play().
# Подкласс Video переопределяет play(), возвращая "Воспроизводится видео".
# Вход: Video()
# Тест: v.play() -> "Воспроизводится видео"

# Задание 19
# Создайте класс Writer с методом write().
# Подкласс Blogger должен переопределять write() и возвращать "Пишет пост для блога".
# Вход: Blogger()
# Тест: b.write() -> "Пишет пост для блога"

# Задание 20
# Создайте класс Plant с атрибутом type.
# Подкласс Flower должен добавлять метод bloom(), возвращающий "Цветок распустился".
# Вход: Flower("Роза")
# Тест: f.bloom() -> "Цветок распустился"

# Задание 21
# Создайте класс Account с методом login(), возвращающим "Вход в аккаунт".
# Подкласс PremiumAccount переопределяет login(), возвращая "Вход в премиум-аккаунт".
# Вход: PremiumAccount()
# Тест: acc.login() -> "Вход в премиум-аккаунт"

# Задание 22
# Создайте класс Food с атрибутом calories.
# Подкласс Pizza должен добавлять атрибут toppings и метод describe().
# Вход: Pizza(300, ["сыр", "помидоры"])
# Тест: pizza.describe() -> "Пицца с начинками: сыр, помидоры"

# Задание 23
# Создайте класс Teacher с методом teach().
# Подкласс MathTeacher должен переопределять teach() и возвращать "Преподаёт математику".
# Вход: MathTeacher()
# Тест: mt.teach() -> "Преподаёт математику"

# Задание 24
# Создайте класс Account с атрибутом email.
# Подкласс VerifiedAccount должен добавлять атрибут verified и метод status().
# Вход: VerifiedAccount("test@mail.com", True)
# Тест: acc.status() -> "Почта test@mail.com подтверждена"

# Задание 25
# Создайте класс Animal с методом move().
# Подкласс Fish должен переопределять move(), возвращая "Плавает в воде".
# Вход: Fish()
# Тест: f.move() -> "Плавает в воде"

# Задание 26
# Создайте класс BankAccount с приватным атрибутом __balance.
# Реализуйте методы deposit(amount) и get_balance().
# Вход: BankAccount(1000), deposit(500)
# Тест: get_balance() -> 1500

# Задание 27
# Создайте класс User с приватным атрибутом __password.
# Реализуйте метод check_password(password), который возвращает True/False.
# Вход: User("Dima", "12345"), check_password("12345")
# Тест: True

# Задание 28
# Создайте класс Product с приватным атрибутом __price.
# Реализуйте метод set_price(price), который обновляет цену.
# Вход: Product("Яблоко", 20), set_price(25)
# Тест: get_price() -> 25

# Задание 29
# Создайте класс Employee с приватным атрибутом __salary.
# Реализуйте методы set_salary(salary) и get_salary().
# Вход: Employee("Иван", 50000), set_salary(60000)
# Тест: get_salary() -> 60000

# Задание 30
# Создайте класс Book с приватным атрибутом __author.
# Реализуйте метод get_author(), возвращающий имя автора.
# Вход: Book("Python 101", "Smith")
# Тест: get_author() -> "Smith"

# Задание 31
# Создайте класс Car с приватным атрибутом __speed.
# Реализуйте методы accelerate(amount) и get_speed().
# Вход: Car(50), accelerate(20)
# Тест: get_speed() -> 70

# Задание 32
# Создайте класс Student с приватным атрибутом __grade.
# Реализуйте методы set_grade(grade) и get_grade().
# Вход: Student("Петя", 4), set_grade(5)
# Тест: get_grade() -> 5

# Задание 33
# Создайте класс Account с приватным атрибутом __email.
# Реализуйте методы set_email(email) и get_email().
# Вход: Account("test@mail.com")
# Тест: get_email() -> "test@mail.com"

# Задание 34
# Создайте класс Device с приватным атрибутом __status.
# Реализуйте метод turn_on(), который устанавливает статус "Включен".
# Вход: Device()
# Тест: после turn_on(), get_status() -> "Включен"

# Задание 35
# Создайте класс Library с приватным списком __books.
# Реализуйте методы add_book(title) и list_books().
# Вход: Library(), add_book("Python"), add_book("Django")
# Тест: list_books() -> ["Python", "Django"]

# Задание 36
# Создайте класс Box с приватным атрибутом __items.
# Реализуйте методы add_item(item) и get_items().
# Вход: Box(), add_item("ручка")
# Тест: get_items() -> ["ручка"]

# Задание 37
# Создайте класс Wallet с приватным атрибутом __cash.
# Реализуйте методы add_cash(amount) и get_cash().
# Вход: Wallet(100), add_cash(50)
# Тест: get_cash() -> 150

# Задание 38
# Создайте класс Door с приватным атрибутом __is_locked.
# Реализуйте методы lock() и is_locked().
# Вход: Door(), lock()
# Тест: is_locked() -> True

# Задание 39
# Создайте класс Account с приватным атрибутом __username.
# Реализуйте метод get_username().
# Вход: Account("user123")
# Тест: get_username() -> "user123"

# Задание 40
# Создайте класс House с приватным атрибутом __address.
# Реализуйте методы set_address(address) и get_address().
# Вход: House(), set_address("Main St, 123")
# Тест: get_address() -> "Main St, 123"

# Задание 41
# Создайте класс Car с приватным атрибутом __fuel_level.
# Реализуйте метод refuel(amount).
# Вход: Car(10), refuel(20)
# Тест: get_fuel_level() -> 30

# Задание 42
# Создайте класс Document с приватным атрибутом __content.
# Реализуйте метод read() и write(new_content).
# Вход: Document("draft"), write("final")
# Тест: read() -> "final"

# Задание 43
# Создайте класс Thermometer с приватным атрибутом __temperature.
# Реализуйте методы set_temperature(temp) и get_temperature().
# Вход: Thermometer(), set_temperature(36.6)
# Тест: get_temperature() -> 36.6

# Задание 44
# Создайте класс User с приватным атрибутом __notifications.
# Реализуйте метод add_notification(note) и get_notifications().
# Вход: User(), add_notification("Привет!")
# Тест: get_notifications() -> ["Привет!"]

# Задание 45
# Создайте класс Car с приватным атрибутом __model.
# Реализуйте методы set_model(model) и get_model().
# Вход: Car(), set_model("Tesla")
# Тест: get_model() -> "Tesla"

# Задание 46
# Создайте класс Account с приватным атрибутом __balance.
# Реализуйте метод withdraw(amount), который уменьшает баланс.
# Вход: Account(1000), withdraw(200)
# Тест: get_balance() -> 800

# Задание 47
# Создайте класс Server с приватным атрибутом __status.
# Реализуйте метод start(), который устанавливает статус "Работает".
# Вход: Server(), start()
# Тест: get_status() -> "Работает"

# Задание 48
# Создайте класс Cat с приватным атрибутом __mood.
# Реализуйте методы set_mood(mood) и get_mood().
# Вход: Cat(), set_mood("Счастлив")
# Тест: get_mood() -> "Счастлив"

# Задание 49
# Создайте класс Playlist с приватным атрибутом __songs.
# Реализуйте методы add_song(title) и list_songs().
# Вход: Playlist(), add_song("Song1"), add_song("Song2")
# Тест: list_songs() -> ["Song1", "Song2"]

# Задание 50
# Создайте класс Teacher с приватным атрибутом __subject.
# Реализуйте методы set_subject(subject) и get_subject().
# Вход: Teacher(), set_subject("Физика")
# Тест: get_subject() -> "Физика"

# Задание 51
# Создайте класс Animal с методом speak().
# Создайте подклассы Dog и Cat, которые по-разному реализуют speak().
# Вход: [Dog("Бобик"), Cat("Мурка")]
# Тест: вызов speak() у каждого должен возвращать разный результат.

# Задание 52
# Создайте класс Shape с методом area().
# Создайте подклассы Circle и Rectangle, которые по-разному реализуют area().
# Вход: [Circle(3), Rectangle(4, 5)]
# Тест: area() возвращает площадь соответствующей фигуры.

# Задание 53
# Создайте класс Vehicle с методом move().
# Подклассы Car и Bike реализуют move() по-своему.
# Вход: [Car(), Bike()]
# Тест: вызов move() у каждого объекта возвращает разный результат.

# Задание 54
# Создайте класс Writer с методом write().
# Подклассы Blogger и Journalist реализуют write() по-разному.
# Вход: [Blogger(), Journalist()]
# Тест: разные строки при вызове write().

# Задание 55
# Создайте класс Payment с методом pay().
# Подклассы CreditCard и PayPal реализуют pay() по-разному.
# Вход: [CreditCard(), PayPal()]
# Тест: вызов pay() возвращает разные способы оплаты.

# Задание 56
# Создайте класс Worker с методом work().
# Подклассы Developer и Designer реализуют work() по-своему.
# Вход: [Developer(), Designer()]
# Тест: вызов work() выводит разные строки.

# Задание 57
# Создайте класс Animal с методом make_sound().
# Подклассы Cow и Duck реализуют make_sound() по-разному.
# Вход: [Cow(), Duck()]
# Тест: разные звуки.

# Задание 58
# Создайте класс Appliance с методом turn_on().
# Подклассы Fridge и Microwave переопределяют turn_on() по-разному.
# Вход: [Fridge(), Microwave()]
# Тест: разные фразы.

# Задание 59
# Создайте класс Shape с методом draw().
# Подклассы Triangle и Square по-разному рисуют фигуру.
# Вход: [Triangle(), Square()]
# Тест: draw() возвращает разные строки.

# Задание 60
# Создайте класс Document с методом print_doc().
# Подклассы PDF и WordDoc реализуют print_doc() по-разному.
# Вход: [PDF(), WordDoc()]
# Тест: разные строки.

# Задание 61
# Создайте класс Sport с методом play().
# Подклассы Football и Basketball реализуют play() по-своему.
# Вход: [Football(), Basketball()]
# Тест: play() выводит разные строки.

# Задание 62
# Создайте класс Animal с методом sleep().
# Подклассы Dog и Cat реализуют sleep() по-разному.
# Вход: [Dog(), Cat()]
# Тест: sleep() выводит разные строки.

# Задание 63
# Создайте класс MusicInstrument с методом play_sound().
# Подклассы Piano и Drum реализуют play_sound() по-своему.
# Вход: [Piano(), Drum()]
# Тест: play_sound() возвращает разные звуки.

# Задание 64
# Создайте класс Shape с методом color().
# Подклассы Circle и Triangle задают цвет по-разному.
# Вход: [Circle(), Triangle()]
# Тест: color() возвращает разные строки.

# Задание 65
# Создайте класс Gadget с методом use().
# Подклассы Phone и Tablet реализуют use() по-разному.
# Вход: [Phone(), Tablet()]
# Тест: use() возвращает разные строки.

# Задание 66
# Создайте класс Employee с методом daily_task().
# Подклассы Manager и Developer реализуют daily_task() по-разному.
# Вход: [Manager(), Developer()]
# Тест: разные строки.

# Задание 67
# Создайте класс Notification с методом send().
# Подклассы SMS и Email реализуют send() по-разному.
# Вход: [SMS(), Email()]
# Тест: send() возвращает разные способы уведомления.

# Задание 68
# Создайте класс PaymentMethod с методом process().
# Подклассы Cash и Crypto реализуют process() по-разному.
# Вход: [Cash(), Crypto()]
# Тест: process() возвращает разные строки.

# Задание 69
# Создайте класс GameCharacter с методом attack().
# Подклассы Warrior и Mage реализуют attack() по-разному.
# Вход: [Warrior(), Mage()]
# Тест: attack() возвращает разные строки.

# Задание 70
# Создайте класс Shape с методом scale(factor).
# Подклассы Circle и Rectangle по-разному масштабируют себя.
# Вход: [Circle(3), Rectangle(4, 5)]
# Тест: scale(2) у каждого возвращает разный результат.

# Задание 71
# Создайте класс Media с методом play().
# Подклассы Audio и Video реализуют play() по-разному.
# Вход: [Audio(), Video()]
# Тест: play() возвращает разные строки.

# Задание 72
# Создайте класс Report с методом generate().
# Подклассы SalesReport и FinanceReport реализуют generate() по-разному.
# Вход: [SalesReport(), FinanceReport()]
# Тест: generate() возвращает разные отчеты.

# Задание 73
# Создайте класс Account с методом access().
# Подклассы UserAccount и GuestAccount реализуют access() по-разному.
# Вход: [UserAccount(), GuestAccount()]
# Тест: access() возвращает разные уровни доступа.

# Задание 74
# Создайте класс Animal с методом move().
# Подклассы Snake и Kangaroo реализуют move() по-разному.
# Вход: [Snake(), Kangaroo()]
# Тест: move() возвращает "ползёт" или "прыгает".

# Задание 75
# Создайте класс Employee с методом report().
# Подклассы Engineer и Designer реализуют report() по-разному.
# Вход: [Engineer(), Designer()]
# Тест: report() возвращает разные строки.

# Задание 76
# Создайте абстрактный класс Animal с абстрактным методом make_sound().
# Подклассы Dog и Cat реализуют make_sound() по-разному.
# Вход: [Dog("Бобик"), Cat("Мурка")]
# Тест: dog.make_sound() -> "Гав", cat.make_sound() -> "Мяу"

# Задание 77
# Создайте абстрактный класс Vehicle с абстрактным методом move().
# Подклассы Car и Bike реализуют move() по-своему.
# Вход: [Car("Toyota"), Bike("Yamaha")]
# Тест: car.move() -> "Машина Toyota едет", bike.move() -> "Мотоцикл Yamaha едет"

# Задание 78
# Создайте абстрактный класс Shape с абстрактным методом area().
# Подклассы Rectangle и Circle реализуют area().
# Вход: [Rectangle(4, 5), Circle(3)]
# Тест: правильная площадь.

# Задание 79
# Создайте абстрактный класс Payment с абстрактным методом pay().
# Подклассы CardPayment и CashPayment реализуют pay().
# Вход: [CardPayment(), CashPayment()]
# Тест: pay() выводит способ оплаты.

# Задание 80
# Создайте абстрактный класс Employee с абстрактным методом work().
# Подклассы Developer и Manager реализуют work().
# Вход: [Developer(), Manager()]
# Тест: work() выводит разные строки.

# Задание 81
# Создайте абстрактный класс Media с абстрактным методом play().
# Подклассы Audio и Video реализуют play().
# Вход: [Audio(), Video()]
# Тест: play() возвращает "Воспроизводим аудио" и "Воспроизводим видео"

# Задание 82
# Создайте абстрактный класс Appliance с абстрактным методом turn_on().
# Подклассы Oven и Fridge реализуют turn_on().
# Вход: [Oven(), Fridge()]
# Тест: turn_on() возвращает разные строки.

# Задание 83
# Создайте абстрактный класс Shape с абстрактным методом draw().
# Подклассы Triangle и Square реализуют draw().
# Вход: [Triangle(), Square()]
# Тест: draw() возвращает разные строки.

# Задание 84
# Создайте абстрактный класс User с абстрактным методом access_level().
# Подклассы Admin и Guest реализуют access_level().
# Вход: [Admin(), Guest()]
# Тест: разные уровни доступа.

# Задание 85
# Создайте абстрактный класс Report с абстрактным методом generate().
# Подклассы SalesReport и InventoryReport реализуют generate().
# Вход: [SalesReport(), InventoryReport()]
# Тест: generate() возвращает разные отчёты.

# Задание 86
# Создайте абстрактный класс Instrument с абстрактным методом play_sound().
# Подклассы Guitar и Piano реализуют play_sound().
# Вход: [Guitar(), Piano()]
# Тест: разные звуки.

# Задание 87
# Создайте абстрактный класс Notification с абстрактным методом send().
# Подклассы SMS и Email реализуют send().
# Вход: [SMS(), Email()]
# Тест: send() возвращает разные строки.

# Задание 88
# Создайте абстрактный класс Animal с абстрактным методом sleep().
# Подклассы Cat и Dog реализуют sleep() по-разному.
# Вход: [Cat(), Dog()]
# Тест: sleep() возвращает разные строки.

# Задание 89
# Создайте абстрактный класс Device с абстрактным методом start().
# Подклассы Laptop и Phone реализуют start().
# Вход: [Laptop(), Phone()]
# Тест: start() возвращает "Запуск ноутбука" и "Запуск телефона".

# Задание 90
# Создайте абстрактный класс Shape с абстрактным методом perimeter().
# Подклассы Circle и Rectangle реализуют perimeter().
# Вход: [Circle(3), Rectangle(4, 5)]
# Тест: правильный периметр.

# Задание 91
# Создайте абстрактный класс Worker с абстрактным методом do_work().
# Подклассы Engineer и Designer реализуют do_work().
# Вход: [Engineer(), Designer()]
# Тест: разные строки.

# Задание 92
# Создайте абстрактный класс Message с абстрактным методом send().
# Подклассы SMS и Push реализуют send().
# Вход: [SMS(), Push()]
# Тест: разные строки.

# Задание 93
# Создайте абстрактный класс Plant с абстрактным методом grow().
# Подклассы Tree и Flower реализуют grow().
# Вход: [Tree(), Flower()]
# Тест: grow() возвращает "Дерево растёт" и "Цветок растёт".

# Задание 94
# Создайте абстрактный класс GameCharacter с абстрактным методом attack().
# Подклассы Knight и Archer реализуют attack().
# Вход: [Knight(), Archer()]
# Тест: attack() возвращает разные строки.

# Задание 95
# Создайте абстрактный класс Account с абстрактным методом login().
# Подклассы UserAccount и GuestAccount реализуют login().
# Вход: [UserAccount(), GuestAccount()]
# Тест: login() возвращает разные строки.

# Задание 96
# Создайте абстрактный класс Transport с абстрактным методом start_engine().
# Подклассы Car и Boat реализуют start_engine().
# Вход: [Car(), Boat()]
# Тест: start_engine() возвращает разные строки.

# Задание 97
# Создайте абстрактный класс Payment с абстрактным методом process().
# Подклассы Card и Cash реализуют process().
# Вход: [Card(), Cash()]
# Тест: разные способы оплаты.

# Задание 98
# Создайте абстрактный класс Shape с абстрактным методом resize(factor).
# Подклассы Circle и Rectangle реализуют resize().
# Вход: [Circle(3), Rectangle(4, 5)], factor=2
# Тест: новые размеры.

# Задание 99
# Создайте абстрактный класс Notification с абстрактным методом notify().
# Подклассы PushNotification и EmailNotification реализуют notify().
# Вход: [PushNotification(), EmailNotification()]
# Тест: разные строки.

# Задание 100
# Создайте абстрактный класс Animal с абстрактным методом move().
# Подклассы Fish и Bird реализуют move().
# Вход: [Fish(), Bird()]
# Тест: move() возвращает "Плавает" и "Летает"
