son = int(input("Son kiriting: "))

teskari_son = 0

while son > 0:
    last = son % 10
    teskari_son = teskari_son * 10 + last
    son = son // 10

print(f"Teskari tartibda: {teskari_son}")
