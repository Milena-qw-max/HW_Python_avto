from address import Address
from mailing import Mailing


address_from = Address("123456", "Москва", "Ленина", "10", "25")
address_to = Address("654321", "Санкт-Петербург", "Невский", "20", "1")


mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=500.00,
    track="RU123456789CN"
)


print(
    f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. "
    f"Стоимость {mailing.cost} рублей."
)
