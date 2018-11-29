import random as rnd

# Showing rules at the start of the game
def showRules():
    print("Привет, поиграем в города?")
    print("Правила игры:")
    print("1. Называешь город на последнюю букву названного города")
    print("2. Города не должны повторяться")
    print("3. Если хочешь сдаться, введи стоп-слово: End")
    print("Давай сыграем!\n")

# Showing used cities at the end of the game
def showResults(usedCities):
    print("\n\nИспользованные города:")
    print(used[:-1])

# Looking for words with space or hyphen
def hardWord(city):
    space = ' '
    hyphen = '-'
    if space in city or hyphen in city:
        return True
    return False

# Checking player's city by 3 rules
def checkRules(newCity, lastCity, usedCities, allCities):
    modifiedNewCity = newCity[0].upper() + newCity[1:].lower()
    if hardWord(newCity):
        i = 0
        for letter in modifiedNewCity:
            if letter == ' ' or letter == '-':
                modifiedNewCity = modifiedNewCity[:i + 1] + modifiedNewCity[i + 1].upper() + modifiedNewCity[i + 2:]
            i += 1

    if lastCity == '' and modifiedNewCity in allCities:
        return True
    elif modifiedNewCity not in allCities:
        print("Этого города не существует!")
        return False
    elif newCity.lower() in usedCities:
        print("Этот город уже называли!")
        return False
    elif lastCity[len(lastCity) - 1].lower() == 'ь' or lastCity[len(lastCity) - 1].lower() == 'ъ' or lastCity[len(lastCity) - 1].lower() == 'ы':
        mLastCity = lastCity[:-1]
        if newCity[0].lower() == mLastCity[len(mLastCity) - 1].lower():
            return True
        else:
            return False
    elif newCity[0].lower() != lastCity[len(lastCity) - 1].lower():
        print("Этот город не подходит!")
        return False
    else:
        return True

# Creating player's city ang going to check it
def new(lastCity, usedCities, allCities):
    ans = input("Введи свой город: ")
    if ans.lower() == 'end':
        return 'end'
    if checkRules(ans, lastCity, usedCities, allCities):
        return ans
    else:
        return new(lastCity, usedCities, allCities)


showRules()
cities = []
next = ''
last = ''
used = []
# Rewriting all cities to a list for more comfort
with open('DB_cities.txt', 'r') as allCities:
    for city in allCities:
        cities.append(city.replace('\n', ''))

# Choosing whoos turn is first
if rnd.randint(0, 1) == 0:
    print("Первым ходит компьютер: ")
    city = cities[rnd.randint(0, len(cities) - 1)]
    print(city)

    mCity = city.lower()
    last = mCity
    used.append(mCity)
else:
    print("Вы ходите первым!")

# Starting the game
while next != 'end':
    # Player's turn
    next = new(last, used, cities)
    last = next.lower()
    used.append(last)

    # Bot's turn
    numCity = 0
    for city in cities:
        numCity += 1
        mCity = city.lower()
        if last[len(last) - 1] == 'ъ' or last[len(last) - 1] == 'ы' or last[len(last) - 1] == 'ь':
            last = last[:-1]
        if city[0].lower() == last[len(last) - 1].lower() and mCity not in used:
            print(city)
            last = mCity
            used.append(mCity)
            break
        if numCity == len(cities):
            print("Ура! Ты победил!")
            next = 'end'
            used.append('end')

showResults(used)
