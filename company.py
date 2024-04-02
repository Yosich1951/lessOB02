"""
Программа представляет собой систему управления учетными записями пользователей
для небольшой компании.
Компания разделяет сотрудников на обычных работников и администраторов.
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. А
дминистраторы, помимо обычных данных пользователей, имеют дополнительный уровень
доступа и могут добавлять или удалять пользователя из системы.
"""


class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Уникальный идентификатор пользователя
        self._name = name  # Имя пользователя
        self._access_level = 'user'  # Уровень доступа обычного пользователя

    # Метод для получения идентификатора пользователя
    def get_user_id(self):
        return self._user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self._name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self._access_level

    # Метод для установки имени пользователя (может понадобиться при изменении данных)
    def set_name(self, name):
        self._name = name

class Admin(User):  # Наследование от класса User для администратора
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Дополнительный уровень доступа для администратора

    # Метод для добавления пользователя в систему
    def add_user(self, users_list, user):
        users_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    # Метод для удаления пользователя из системы
    def remove_user(self, users_list, user):
        users_list.remove(user)
        print(f"Пользователь {user.get_name()} удалён.")


# Создание списка пользователей
users_list = []

# Создание экземпляра администратора
admin = Admin("1", "Админ Иванов")


# Примеры использования:

# Создание обычных пользователей
user1 = User("2", "Петров Петр")
user2 = User("3", "Сидоров Сидор")
user3 = User("4", "Кузнецов Сергей")
print(user1.get_user_id())
print(user1.get_name())

# Администратор добавляет пользователей в систему
admin.add_user(users_list, user1)
admin.add_user(users_list, user2)
admin.add_user(users_list, user3)

# Вывод информации о пользователях
print('Вывод информации о пользователях')
for user in users_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Администратор удаляет пользователя из системы
admin.remove_user(users_list, user1)

# Проверяем, кто остался в системе
print("\nСписок пользователей после удаления:")
for user in users_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
