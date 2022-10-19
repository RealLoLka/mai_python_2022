drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
for drone in drone_list:
	print(drone)

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

x = input().lower()
i = 0
for drone in (drone_list):
    if drone.lower().find(x) != -1:
        if drone.split(" ")[0].upper() == "DJI":
            i += 1
            print(drone.split(" ")[0].upper() + drone[3::])
        elif drone.split(" ")[0].upper() == "AUTEL":
            i += 1
            print(drone.split(" ")[0].capitalize() + drone[5::])
print('Count =', i)
  
    
#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

F = ['DJI', 'Autel', 'Parrot', 'Ryze', 'Eachine']
DL = []

for drone in (drone_list):
  DL.append(drone.split(" ")[0].upper())

for name in F:
    print(name,": ",DL.count(name.upper()))

print(drone_list)

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

n, m = 0, 0

for drone, weight in zip(drone_list,  drone_weight_list):
  if weight >= 150:
    n += 1
    print("Need registration -", drone)
  else:
    m += 1
    print('No need registration -', drone)
    
print('reg =', n,'noreg =', m)

#TODO4
#для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

n, m = 0, 0
hight = 150
loc = true
nosee = true

for drone, weight in zip(drone_list,  drone_weight_list):
  if hight > 100 or weight > 150 or loc = true or nosee = true :
    n += 1
    print("Need registration -", drone)
  else:
    m += 1
    print('No need registration -', drone)

print('reg =', n,'noreg =', m)


#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine

x = input().lower()
i = 0
for drone in (drone_list):
    if drone.lower().find(x) != -1:
        if drone.split(" ")[0].upper() == "DJI":
            i += 1
            print(drone[4::])
        elif drone.split(" ")[0].upper() == "AUTEL":
            i += 1
            print(drone[6::])
        elif drone.split(" ")[0].upper() == "PARROT":
            i += 1
            print(drone[7::])
        elif drone.split(" ")[0].upper() == "RYZE":
            i += 1
            print(drone[5::])
        elif drone.split(" ")[0].upper() == "EACHINE":
            i += 1
            print(drone[8::])  
print('Count =', i)
