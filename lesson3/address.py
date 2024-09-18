class Address:
    def __init__ (self , index , city , street , house , apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"Индекс: {self.index} , Город : {self.city} , Улица:
{self.street} , Дом: {self.house} , Квартира: {self.apartment}"
