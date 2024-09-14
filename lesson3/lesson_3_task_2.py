from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Sansung" , "Galaxy S20 Ultra" , "+79083003214"))
catalog.append(Smartphone("Apple" , "iPhone 14" , "+79188654535"))
catalog.append(Smartphone("Xiaomi" , "Mi 5T" , "+79134451234"))
catalog.append(Smartphone("Huawei" , "Nova 5T" , "+79155567686"))
catalog.append(Smartphone("OnePlus" , "10t" , "+79085674535"))

for smartphone in catalog :
    print(smartphone)