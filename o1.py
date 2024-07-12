import os
os.system("cls")

users = [
    {
        'name': 'Eshmat',
        'surname': 'Toshmatov',
        'age': 12,
        'height': 160,
        'nation': 'uzbek',
        'weight': 55
    },
    {
        'name': 'Sarvar',
        'surname': 'Qodirov',
        'age': 15,
        'height': 166,
        'nation': 'russian',
        'weight': 57
    },
    {
        'name': 'Laylo',
        'surname': 'Nabieva',
        'age': 14,
        'height': 170,
        'nation': 'turkish',
        'weight': 60
    },
    {
        'name': 'Dilshod',
        'surname': 'Salimov',
        'age': 13,
        'height': 175,
        'nation': 'uzbek',
        'weight': 65
    },
    {
        'name': 'Oygul',
        'surname': 'Ganieva',
        'age': 16,
        'height': 167,
        'nation': 'uyghur',
        'weight': 52
    }
]




with open("users.txt", "w") as file:
    data = file.write().split("\n")

    for i in range(len(data)):
        data[i] = data[i].split("|")

        user = dict()
        user['name'] = data[i][0]
        user['surname'] = data[i][1]
        user['age'] = int(data[i][2])

        users.append(user)


file = open('odamlar.txt', 'w')

for user in users:
    file.write(f"{user['name']}|{user['surname']}|{user['age']}\n")

file.close()


