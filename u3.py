import os
os.system("cls")  

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

temp=sonlar[0]
sonlar[0]=sonlar[9]
sonlar[9]=temp

print(sonlar)