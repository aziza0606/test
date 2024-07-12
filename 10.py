a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a > b:
    a, b = b, a  

new = a
count = 0
last1 = last2 = last3 = None

while new <= b:
    if new % 2 == 0:
        last1, last2, last3 = last2, last3, new
        count += 1
    new += 1


if count < 3:
    print("Juft sonlar yetarli emas")
else:
    print("Oxirgi 3 ta juft son: ", last1, last2, last3)
