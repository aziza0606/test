from os import system
system("cls")

def key_value_set(dct):
    key_value_set=set()
    for key,value in dct.items():
        key_value_set.add((key,value))
    return key_value_set


dct = {'a': 10, 'b': 20, 'c': 30}
natija=key_value_set(dct)
print(natija)