import os
os.system("cls")

kitoblar = []

with open("books.txt", "r") as file:
    data = file.read().split("\n")
    
    for line in data:
        if line.strip(): 
            parts = line.split(", ")
            nomi = parts[0].strip()
            muallif = parts[1].strip()
            yil = int(parts[2].strip())
            narxi = int(parts[3].strip())
            kitob = {
                'nomi': nomi,
                'muallif': muallif,
                'yil': yil,
                'narxi': narxi
            }
            if muallif == "J.K. Rowling" and narxi > 20:
                kitoblar.append(kitob)

with open("expensive_rowling_books.txt", "w") as expensive_rowling_booksFile:
    for kitob in kitoblar:
        expensive_rowling_booksFile.write(f"{kitob['nomi']}, {kitob['muallif']}, {kitob['yil']}, {kitob['narxi']}\n")
