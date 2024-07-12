import os
os.system("cls")

aholilar=[]

with open("aholi.txt","r") as file:
    data=file.readlines()
    
    for line in data:
        if line.split():
            parts=line.split(",")
            nomi=parts[0].split()
            aholi=int(parts[1].strip())
            tili=parts[2].split()

            aholi={
                'nomi':nomi,
                'aholi':aholi,
                'tili':tili
               }
            if aholi['aholi']>1000000:
                aholilar.append(aholi)
with open("mamlakatlar.txt","w") as mamlakatlarFile:
    for aholi in aholilar:
        mamlakatlarFile.write(f"{aholi['nomi']},{aholi['aholi']},{aholi['tili']}\n")