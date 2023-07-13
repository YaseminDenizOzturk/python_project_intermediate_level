class Cmp:
    def __init__(self):
        # self parametresi oluşturulan ürünleri temsil eder.
        self.name = "A"
        self.price = "20000"
        print("Cmp nesnesi oluşturuldu.")

cmp_1 = Cmp()
cmp_2 = Cmp()

print(cmp_1.name,cmp_1.price)
print(cmp_2.name,cmp_2.price)
# iki kez aynı şeyi yazdıracaktır çünkü __init__ fonksiyonu iki kez çağırıldı.


class Phone:
    def __init__(self,name,price,isActive,n=32):
        # her seferinde değer girmek yerine bazılarına default değer de atayabilirim.
        # n=32 de default değer atadım artık değiştirilmediği sürece n varsayılan olarak 32 
        self.name = name
        self.price = price
        self.isActive = isActive
        self.n = n
        print("Phone nesensi oluşturuldu.")
        # yani üsteki classtaki initten farklı olarak burada artık bir nesne oluşturduğumuzda name ve price değerlerini vermemiz gerekiyor.


first_phone = Phone("name1","price1","True")
second_phone = Phone("name2","pirce2","True")
third_phone = Phone("name3","price3","False")

print(first_phone.name,first_phone.price,first_phone.isActive,first_phone.n)
print(second_phone.name,second_phone.price,second_phone.isActive,second_phone.n)
print(third_phone.name,third_phone.price,third_phone.isActive,third_phone.n)

