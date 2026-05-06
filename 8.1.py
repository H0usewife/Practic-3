# 8.1

countries = {
    "Россия": "Москва",
    "Япония": "Токио",
    "Тайланд": "Бангкок",
    "Китай": "Пекин"
}

print("Страны и столицы:")

for country, capital in countries.items():
    print(country, "-", capital)

country_name = input("Введите название страны: ")

if country_name in countries:
    print("Столица:", countries[country_name])
else:
    print("Такой страны нет")

print("Словарь по алфавиту:")

for country in sorted(countries):
    print(country, "-", countries[country])