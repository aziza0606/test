import os
os.system("clear")

son=int(input("3 xonali son kiriting:"))

onlik=(son//10)%10
birlik=son%10
yuzlik=son//100

new=int(str(yuzlik)+str(birlik)+str(onlik))

print(new)