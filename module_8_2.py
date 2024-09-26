# Задача "План перехват":

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        if isinstance(i, int | float):
            result += i
        else:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        long = (len(numbers))
    except:
        print('В numbers записан некорректный тип данных')
        return

    itog = personal_sum(numbers)
    try:
        avr = itog[0] / (long - itog[1])
    except:
        return 0
    return avr


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать"""
