import random


class PersonData:
    user_name = 'Мария Кислицына'
    login = 'mariakislitsyna16123@yandex.ru'
    password = 'mariakislitsyna16123@yandex.ru'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"