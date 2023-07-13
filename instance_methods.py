class User:

    def __init__(self,_username,name,surname,birthday):
        # def init aslında bir constructor
        # object attribute , instance attribute

        self.username = _username
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def info(self):
        return f"{self.username} kullanıcı adıyla {self.name} {self.surname} sisteme kaydınız başarılı."
        # instance methods
        # sadece objeye özel kullanıcıya özel mesaj verdim.

    def calculateAge(self):
        return f"kullanıcı {self.username} {2022 - self.birthday} yaşında"

user_1 = User("merve233","Merve","Ozturk",2002)
user_2 = User("elif5","Elif","Ozturk",2000)


print(user_1.info())
print(user_2.info())

print(user_1.calculateAge())
print(user_2.calculateAge())


