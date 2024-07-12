import os
os.system("clear")

sekund=int(input("sekundlarni kiriting:"))


soat = sekund // 3600

sekund = sekund - soat * 3600

minut = sekund // 60

sekund = sekund - minut * 60;



print(soat,"soat")
print(minut,"minut")
print(sekund,"sekund")