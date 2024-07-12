import os
os.system("clear")

sekund=int(input("sekundlarni kiriting:"))

soat = sekund // 3600
qolgan_sekund = sekund % 3600


print(soat,"soat")
print(qolgan_sekund,"sekund")