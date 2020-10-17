import random

stats_names = ["strength", "dexterity", "intelligence", "wisdom","charisma"]
stats =[]
attributes = 5
for i in range(attributes):
    r = random.randint(60, 80)
    stats.append(r)

print(stats_names)
print("Статы персонажа: ",stats)

select = int(input('Выберите номер статы для увеличения(1-5): '))
select -= 1
stats[select] = stats[select] + random.randint(5, 15)
for i in range(len(stats)):
    if i == select:
        continue
    stats[i] = stats[i] - random.randint(5, 15)

print("Статы персонажа: ",stats)

fireball = [12, 15, 28, 10, 5]
lightning = [7, 13, 15, 30, 10]
silence = [23, 10, 12, 7, 18]
fire_ward = [ 20, 23, 14, 6, 17]

while True:
    print("-------------------------------------")
    print("[f] - fireball\n[l] - lightnnig\n[s] - silence\n[fw] - fire ward")
    weapon = input("Выберете оружие: ")
    if weapon == "f":
        print("Сила оружия: ",fireball)
    if weapon == "l":
        print("Сила оружия: ", lightning)
    if weapon == "s":
        print("Сила оружия :",silence)
    if weapon == "fw":
        print("Сила оружия :", fire_ward)

    s = 0
    for i in range (len(stats)):
        if weapon == "f":
            stats[i] = stats[i] - fireball[i]
        if weapon == "l":
            stats[i] = stats[i] - lightning[i]
        if weapon == "s":
            stats[i] = stats[i] - silence[i]
        if weapon == "fw":
            stats[i] = stats[i] - fire_ward[i]
        if stats[i] <= 0:
            stats[i] = 0
            s += 1
    print("Статы персонажа: ",stats)

    if s == 5:
        print("Статы закончились!!!")
        break
