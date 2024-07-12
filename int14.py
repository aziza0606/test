import os
os.system("clear")

son=int(input("3 xonali son kiriting:"))

num1=son%10
last=son//10
new=int(str(num1)+str(last))

print(new)