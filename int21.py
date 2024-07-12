import os
os.system("clear")

sekund=int(input("sekundlarni kiriting:"))


minut=sekund//60
qolgan_sekund=sekund%60


print(minut,"minut")
print(qolgan_sekund,"sekund")