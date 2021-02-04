finance = float(input('Введите оборот фирмы'))
expenses = float(input('Введите издержки фирмы '))
if finance > expenses:
    print(f"Прибыль!.Выручки составила {finance / expenses:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника: {finance / workers:.2f}")
elif finance == expenses:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
