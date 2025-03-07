from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79031234567"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79219876543"))
catalog.append(Smartphone("Google", "Pixel 7", "+79055551212"))
catalog.append(Smartphone("OnePlus", "11", "+79112223344"))

for smartphone in catalog:
    print(smartphone)


