from mailing import Mailing
from address import Address

mailing = Mailing(
    to_address =Address("23456" , "Москва" , "Солянка" , "25" , "35"),
    from_address=Address('12345' , "Санкт-Петербург" , "Лермонтовский проспект" , "3" , "15"),
    cost=1000,
    track= "1234567890"
)

print(mailing)