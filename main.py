## Модуль ввода и обработки данных
print("Введите данные из руководства по эксплуатации вашего автомобиля об интервале замены моторного масла (в км) :")
while True:
    try:
        BaseInterval = int(input())
        if BaseInterval <= 0:
            print("Ошибка: Введено неверное число. Повторите ввод. ")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите тип вашего масла (минеральное, синтетическое или полусинтетическое)?")
OilType = input().lower()
ListOilTypes = ["минералка", "минеральное", "минеральный", "минер",
                "синт", "синтетика", "синтетическое", "синтетический",
                "полусинт", "полусинтетика", "полусинтетическое", "полусинтетический"]
if OilType not in ListOilTypes:
    print(
        "Ошибка. Выберите и выведите № типа вашего масла, где 1 - синтетическое, 2 - минеральное, 3 - полусинтетическое :")
    OilType = int(input())
    while OilType < 1 or OilType > 3:
        print(
            "Выберите и выведите № типа вашего масла, где 1 - синтетическое, 2 - минеральное, 3 - полусинтетическое :")
        try:
            OilType = int(input())
        except ValueError:
            print("Ошибка: Введено не число. Повторите ввод.")
            OilType = 0
            if OilType < 1 or OilType > 3 and OilType != 0:
                print("Ошибка: Введите число от 1 до 3.")

print("Введите субъективную оценку качества вашего масла (от 1 до 10):")

while True:
    try:
        OilQual = int(input())
        if OilQual > 10 or OilQual < 1:
            print("Введите данные в диапозоне от 1 до 10 включительно :")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print(
    "Введите данные о проценте времени, когда двигатель вашего автомобиля работает при более 75% от крутящего момента (буксировки, горные дороги, движение с полной загрузкой) :")
while True:
    try:
        OverloadTime = int(input())
        if OverloadTime < 0 or OverloadTime > 100:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите данные о том, какой процент времени вы находитесь в пробках:")
while True:
    try:
        JamTime = int(input())
        if JamTime > 100 or JamTime < 0:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите процент поездок короче 10 км :")
while True:
    try:
        ShortTrip = int(input())
        if ShortTrip < 0 or ShortTrip > 100:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите процент времени при езде со скоростью больше 125 км/ч :")
while True:
    try:
        FastSpeed = int(input())
        if FastSpeed < 0 or FastSpeed > 100:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите процент резких разгонов :")
while True:
    try:
        HardAccel = int(input())
        if HardAccel < 0 or HardAccel > 100:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите процент резких торможений :")
while True:
    try:
        HardBraking = int(input())
        if HardBraking < 0 or HardBraking > 100:
            print("Ошибка: Введено неверное число. Повторите ввод.")
        else:
            break
    except ValueError:
        print("Ошибка: Введено не число. Повторите ввод.")

print("Введите тип топлива, который вы используете (АИ-100, АИ-95, АИ-92, ДТ) :")
FuelType = input().lower()
ListFuelType = ["100", "95", "92", "дт",
                "аи-100", "аи-95", "аи-92",
                "дизель", "дизельное топливо"]
if FuelType not in ListFuelType:
    print("Ошибка. Выберите и выведите № типа вашего масла, где 1 - АИ-100, 2 - АИ-95, 3 - АИ-92, 4 - ДТ :")
    FuelType = int(input())
    while FuelType < 1 or FuelType > 4:
        print("Выберите и выведите № типа вашего масла, где 1 - АИ-100, 2 - АИ-95, 3 - АИ-92, 4 - ДТ :")
        try:
            FuelType = int(input())
        except ValueError:
            print("Ошибка: Введено не число. Повторите ввод.")
            FuelType = 0
            if FuelType < 1 or FuelType > 4 and FuelType != 0:
                print("Ошибка: Введите число от 1 до 3.")

# Модуль разработки математической модели
minerList = ["минералка", "минеральное", "минеральный", "минер"]
sintList = ["синт", "синтетика", "синтетическое", "синтетический"]
if OilType in minerList or OilType == 2:
    A_oil = 0.5
    B_oil = (OilQual - 10) * 0.03
elif OilType in sintList or OilType == 1:
    A_oil = 1.0
    B_oil = (OilQual / 10) * 0.3
else:
    A_oil = 0.75
    B_oil = (OilQual - 5) * 0.03

K_oil = (A_oil + B_oil) * 0.95

K_overload = 1 - (OverloadTime * 0.002 + JamTime * 0.0015)

K_shortTrip = 1 - (ShortTrip * 0.004)

K_drivestyle = 1 - (FastSpeed * 0.003 + HardAccel * 0.002 + HardBraking * 0.001)

FuelList_100 = ["100", "аи-100"]
FuelList_92 = ["92", "аи-92"]
if FuelType in FuelList_100 or FuelType == 1:
    K_fuelType = 1.1
elif FuelType in FuelList_92 or FuelType == 3:
    K_fuelType = 0.9
else:
    K_fuelType = 1

# Модуль расчета оптимального интервала по замене моторного масла
from math import trunc


def round_to_10(x):
    return (trunc(x) // 10) * 10


OptimalInterval = round_to_10(BaseInterval * K_oil * K_overload * K_shortTrip * K_drivestyle * K_fuelType)

# Модуль вывода оптимального интервала по замене моторного масла
print(f"Ваш оптимальный интервал по замене моторного масла составляет :\n{OptimalInterval:.0f} км ")
