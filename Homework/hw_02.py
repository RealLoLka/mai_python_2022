# Напоминание: вам понадобится материал лекций:
# 3 - Списки и кортежи
# 4 - Словари и множества
# 7 и 8 - Классы
# 9 - Работа с файлами

# =====================================
# ЗАДАНИЕ 1: Работа с файлами
# =====================================
# TODO 1-1
#  Прочитайте данные из файла pilot_path.json (лекция 9)

# ВАШ КОД:
import json
from pprint import pprint


with open("E:/git/python/mai_python_2022/Homework/pilot_path.json") as f:
	pilot_mission_dict = json.load(f)

# with open("C:/Users/4iste/Desktop/Stady/Magistr/1k1s/Github/mai_python_2022/Homework/pilot_path.json") as f:
# 	pilot_mission_dict = json.load(f)


# =====================================
# ЗАДАНИЕ 2: Расчет статистик
# =====================================
# TODO 2-1) Подсчитайте, сколько миссий налетал каждый пилот. Выведите результат в порядке убывания миссий
# ИНФОРМАЦИЯ:
# структура данных в файле: {"имя_пилота": "список_миссий":[миссия1, ...]]
# структура одной миссии: {"drone":"модель_дрона", "mission":[список точек миссии]}
# у пилотов неодинаковое количество миссий (и миссии могут быть разной длины). у каждой миссии - произвольная модель дрона

# РЕЗУЛЬТАТ:
# Пилоты в порядке убывания количества миссий: {'pilot3': 6, 'pilot8': 6, 'pilot6': 5, 'pilot2': 5, 'pilot7': 4, 'pilot9': 3, 'pilot5': 3, 'pilot4': 2, 'pilot1': 1}

# ВАШ КОД:
pilot_dict = {}

for p in pilot_mission_dict.keys():
	pilot_dict[p] = len(pilot_mission_dict[p]['missions'])

# подсказка: готовый код нужной вам сортировки есть здесь (Sample Solution-1:): https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
print(f"Пилоты в порядке убывания количества миссий: {dict(sorted(pilot_dict.items(), key=lambda item: item[1], reverse=True))}")

# TODO 2-2) Получите и выведите список всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: внутри print используйте str.join(), чтобы соединить элементы списка (множества)

# РЕЗУЛЬТАТ:
# Полеты совершались на дронах следующих моделей: DJI Mavic 2 Pro, DJI Mavic 3, DJI Inspire 2, DJI Mavic 2 Zoom, DJI Mavic 2 Enterprise Advanced

# ВАШ КОД:
drone_list = []
lst_mission_dict = list(pilot_dict.items())

for count in lst_mission_dict[:]:
	for c in range(count[1]):
		drone_list.append(pilot_mission_dict[count[0]]['missions'][c]['drone'])


# вывод результата (допишите код)
print(f'Полеты совершались на дронах следующих моделей: {", ".join(set(drone_list))}')



# TODO 2-3) Получите список миссий для каждой модели дронов, которые были в файле pilot_path.json,
# и выведите на экран модель дрона и количество миссий, которые он отлетал

# РЕЗУЛЬТАТ:
# Дрон DJI Inspire 2 отлетал 6 миссий
# Дрон DJI Mavic 2 Pro отлетал 6 миссий
# Дрон DJI Mavic 2 Enterprise Advanced отлетал 10 миссий
# Дрон DJI Mavic 3 отлетал 4 миссий
# Дрон DJI Mavic 2 Zoom отлетал 9 миссий

# ВАШ КОД:
# вывод результата (допишите код)
drone_mis = {}

for drone in set(drone_list):
	print(f'Дрон {drone} отлетал {drone_list.count(drone)} миссий')

# =====================================
# ЗАДАНИЕ 3: Создание классов
# =====================================
# Для вас уже написаны заготовки классов Aircraft и UAV
# TODO 3-1) Добавьте в класс UAV защищенный атрибут _=_missions (тип - список списков [[], []]), куда вы будете сохранять все миссии, которые отлетал беспилотник
# TODO 3-2) При помощи декоратора @property сделайте возможность чтения и записи миссий в этот атрибут (лекция 8)
# TODO 3-3) Создайте в классе UAV публичный метод count_missions, который возвращает количество миссий (лекция 7)
# TODO 3-4) Создайте класс MultirotorUAV - наследник классов Aircraft и UAV (лекция 7)

# ВАШ КОД (дополните то, что нужно в классах):
class Aircraft:
	def __init__(self, weight):
		self._weight = weight

class UAV:
	def __init__(self):
		self._has_autopilot = True
		self._missions = list()

	# напишите код для декоратора атрибута _missions
	@property
	def missions(self):
		return self._missions
	
	@missions.setter
	def missions(self, mis):
		self._missions.append(mis)

	# напишите публичный метод count_missions
	def count_missions(self):
		return len(self._missions)

class MultirotorUAV(Aircraft, UAV):
	def __init__(self, weight, model, brand):
		super().__init__(weight)
		UAV.__init__(self)
		self.__weight = weight
		self.__model = model
		self.__brand = brand

	# напишите публичный метод get_info
	def get_info(self):
		print(f"Инфо: модель {self.get_model()}; бренд: {self.__brand}, масса: {self.__weight}; отлетал {self.count_missions()} миссий")
	# напишите публичный метод get_model
	def get_model(self):
		return self.__model


# =====================================
# ЗАДАНИЕ 4: Работа с экземплярами классов
# =====================================
# TODO 4-1) Создайте экземпляры класса MultirotorUAV для всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: созданные экземпляры класса MultirotorUAV сохраните в список для последующего использования
# TODO 4-2) При создании каждого экземпляра задайте ему как приватные атрибуты массу и производителя из справочника дронов drone_catalog в соответствии с моделью дрона
# TODO 4-3) А также добавьте ему миссии, найденные для этой модели дрона на шаге 2-3
# Напоминание: миссии находятся в атрибуте missions (с декоратором, и поэтому он публично доступен) в классе UAV

# каталог дронов уже готов для вас:
drone_catalog = {
	"DJI Mavic 2 Pro": {"weight":903, "brand":"DJI"},
	"DJI Mavic 2 Zoom": {"weight":900, "brand":"DJI"},
	"DJI Mavic 2 Enterprise Advanced": {"weight":920, "brand":"DJI"},
	"DJI Inspire 2": {"weight":1500, "brand":"DJI"},
	"DJI Mavic 3": {"weight":1000, "brand":"DJI"}
}




drone_clist = []

# ВАШ КОД:
for drone in drone_catalog:
	drone = MultirotorUAV(weight = drone_catalog[drone]["weight"], model = drone , brand = drone_catalog[drone]["brand"])
	for p in pilot_mission_dict:
		for mis in pilot_mission_dict[p]['missions']:
			if drone.get_model() == mis['drone']:
				drone.missions = mis['mission']
	drone_clist.append(drone)




# TODO 4-4
# Напишите код, который выводит информацию по заданной модели дрона. Состав информации: масса, производитель, количество отлетанных миссий
# (название модели пользователь вводит с клавиатуры в любом регистре, но без опечаток)
# Подсказка: для этого вам необходимо вернуться в ЗАДАНИЕ 3 и добавить в класс два публичных метода: get_info(), который выводит нужную информацию,
# и get_model, который позволит получить название модели дрона

# РЕЗУЛЬТАТ:
# Информация о дроне DJI Mavic 2 Pro: масса 903, производитель DJI, количество миссий 6

# ВАШ КОД:
user_unput = input("Введите модель дрона (полностью) в любом регистре\n")
for drone in drone_clist:
	if user_unput.lower() == drone.get_model().lower():
		drone.get_info()