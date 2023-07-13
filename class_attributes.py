class User:

    active_users = 0
    

    def __init__(self,username,name,surname,age):
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
    
# hiç obje oluşturmadan aktif kullanıcı sayısı sıfırdır bunu 20.satırı çalıştırarak görebiliriz.
print(f" Aktif kullanıcı sayısı: {User.active_users}")   
user_1 = User("merve233","Merve","Ozturk",20)
user_2 = User("elif5","Elif","Ozturk",22)
user_3 = User("ayse_61,","ayse","ozturk",40)

print(f" Aktif kullanıcı sayısı: {User.active_users}")   

# programdan çıkış yapan kullanıcı olduğunda
print(user_3.logOut())
print(f" Aktif kullanıcı sayısı: {User.active_users}")

print(user_1.logOut())
print(f" Aktif kullanıcı sayısı: {User.active_users}")

print(user_2.logOut())
print(f" Aktif kullanıcı sayısı: {User.active_users}")


