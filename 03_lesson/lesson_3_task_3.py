from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "15", "24")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "42", "13")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=250,
    track="TRACK123456789"
)

message = (f"Отправление {mailing.track} из "
           f"{mailing.from_address.index}, {mailing.from_address.city}, "
           f"{mailing.from_address.street}, {mailing.from_address.house} - "
           f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
           f"{mailing.to_address.city}, {mailing.to_address.street}, "
           f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
           f"Стоимость {mailing.cost} рублей.")

print(message)
