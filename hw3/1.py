with open('cities.txt', 'r') as cities:
    cities_list = cities.read()

print(cities_list.split('\n'))
cities_list = cities_list.split('\n')

input_population = int(input('Vvedite chislo: '))

new_cities = []

for city in cities_list:
    population = int(city[city.index(':')+1:])

    if population > input_population:
        new_cities.append(city)

print(sorted(new_cities))

with open('new_cities_file', 'w') as new_cities_file:
    for el in sorted(new_cities):
        new_cities_file.write(el+'\n')
    new_cities_file.close()
