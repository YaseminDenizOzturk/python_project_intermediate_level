#class 
#instance,object

class Cmp:
    # olmasını istediğimiz şeyleri metodları veya
    # işlemleri (attribute) burada belirtiyoruz.
    # veya hata vermemesi için ve şimdilik boş bırakmak istiyorsak pass ekleyebiliriz.
    pass


cmp_1 = Cmp()
cmp_2 = Cmp()
print(Cmp)
print(type(Cmp))

#bulunduğu adresi görmek için 
print(cmp_1)
print(cmp_2)


class Phone:
    pass

first_phone = Phone()
second_phone = Phone()
third_phone = Phone()

listPhone = [first_phone,second_phone,third_phone]

# her bir phone nesnesini döngüyle yazdırmak için
for phone in listPhone:
    print(phone)
    print(type(phone))
    # 33. satır yardımıyla her birinin classını da görebiliyoruz.

    






  
