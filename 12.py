x = int(input("son kiriting:"))

if x > 1:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print(f"{x} tub emas.")
            break
    else:
        print(f"{x} tub.")
else:
    print(f"{x} tub emas.")
