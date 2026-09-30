# Написать калькулятор с проверкой деления на ноль и валидацией операций +, −, ×, ÷

while True:
    exit = input("Нажмите Enter, чтобы продолжить, или напишите 'выход', для завершения программы: ").strip()
    if exit == "выход":
        break

    first_number = input("Первое число: ")
    if not first_number.isdigit():
        print("Введите число")
        continue

    operazia = input("Операция: ").strip()
    if operazia not in '+-*/' or operazia == "":
        print("Допустимы только + − × ÷")
        continue

    second_number = input("Второе число: ")
    if not second_number.isdigit():
        print("Введите число")
        continue

    if operazia == "/" and second_number == "0":
        print("Делить на ноль нельзя")
        continue
    answer = 0.0
    if operazia == "+":
        answer = int(first_number) + int(second_number)
    elif operazia == "-":
        answer = int(first_number) - int(second_number)
    elif operazia == "*":
        answer = int(first_number) * int(second_number)
    elif operazia == "/":
        answer = int(first_number) / int(second_number)
    else:
        print("что-то пошло не так")
        continue

    print(f"{first_number} {operazia} {second_number} = {answer}")