class User:

    def __init__(self,user_id,username) :
        self.id = user_id
        self.username = username
        self.followers = 0
        # varsayılan değer olarak sıfır atadım.


first_user = User("012", "yasemin")
print(first_user.id)
print(first_user.username)
print(first_user.followers)

second_user = User("021","deniz")
print(second_user.id)
print(second_user.username)
print(second_user.followers)
