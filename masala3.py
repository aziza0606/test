import os
os.system("cls")

managers = []

with open("employees.txt", "r") as file:
    data = file.read().split("\n")
    
    for line in data:
        if line.strip(): 
            parts = line.split(", ")
            ism = parts[0].strip()
            familiya = parts[1].strip()
            lavozim = parts[2].strip()
            ish_haqi = int(parts[3].strip())
            employee = {
                'ism': ism,
                'familiya': familiya,
                'lavozim': lavozim,
                'ish_haqi': ish_haqi
            }
            if lavozim == "manager":
                managers.append(employee)


with open("managers.txt", "w") as managersFile:
    for manager in managers:
        managersFile.write(f"{manager['ism']}, {manager['familiya']}, {manager['lavozim']}, {manager['ish_haqi']}\n")


print(f"Number of managers: {len(managers)}")
