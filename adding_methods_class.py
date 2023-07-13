class User:

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 
        # followers ve following e varsayılan olarak sıfır atadım.

    def follow(self,user):
        user.followers += 1
        self.following += 1

    # birini takip ettiğimiz zaman takip ettiğimiz kişinin takipçi sayısı 1 artar ve bizim de takip ettiğimiz kişi sayı sayısı 1 artar.

first_user = User("012","yasemin")
second_user = User("021","deniz")

first_user.follow(second_user)

print(first_user.followers)
print(first_user.following)
print(second_user.followers)
print(second_user.following)





        