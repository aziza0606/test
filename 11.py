a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a > b:
    a, b = b, a  

new = a
count = 0
first1 = first2 = first3 = None

while new <= b and count < 3:
    if new % 2 != 0:  
        if count == 0:
            first1 = new
        elif count == 1:
            first2 = new
        elif count == 2:
            first3 = new
        count += 1
    new += 1


if count < 3:
    print("Toq sonlar yetarli emas")
else:
    print("Boshidagi 3 ta toq son: ", first1, first2, first3)
