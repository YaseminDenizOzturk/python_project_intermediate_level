class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Aktif kullanıcı sayısı: {cls.active_users}"

    @classmethod
    def from_string(cls, data_str):
        username, name, surname, age = data_str.split(",")
        return cls(username, name, surname, age)

    def __init__(self, username, name, surname, age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1

    def userName(self):
        return f"{self.username}"

    def logOut(self):
        User.active_users -= 1
        return f"{self.username} kullanıcı çıkış yaptı."


print(User.display_active_users())

user_1 = User("merve233", "Merve", "Ozturk", 20)
user_2 = User("elif5", "Elif", "Ozturk", 22)
user_3 = User("ayse_61,", "ayse", "ozturk", 40)
user_4 = User.from_string("yagmur12,Yagmur,Ozturk,23")

print(User.display_active_users())

print(user_4.username)
print(user_4.name)
print(user_4.surname)
print(user_4.age)
