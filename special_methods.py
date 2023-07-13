class Cmp:
    def __init__(self,cmpMarka,cmpModel,cmpFiyat):
        self.cmpMarka = cmpMarka
        self.cmpModel = cmpModel
        self.cmpFiyat = cmpFiyat

    def __len__(self):
        return self.cmpFiyat
    
    def __str__(self):
        return f"{self.cmpMarka} , {self.cmpModel} ürün listeleniyor... "
       
    
    def __repr__(self):
        return f"{self.cmpMarka} , {self.cmpModel} ürün listeleniyor... "
        
    #str ile repr çıktıları aynıdır.    

cmp_1 = Cmp("X","Y",26000)
print(len(cmp_1))
print(str(cmp_1))
print(repr(cmp_1))

