while True:
    print("Выберите действие: (необходимо скопировать точное название команды)")
    print("сложение, вычитание, умножение, деление, целочисленное деление, остаток от деления, возведение в степень, сравнение чисел, логические операции, проверка принадлежности, проверка тождественности")
    choice = input("Ваш выбор: ")

    if choice in ("сложение", "вычитание", "умножение", "деление", "целочисленное деление", "остаток от деления", "возведение в степень"):
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            if choice == "сложение":
                print(a + b)
            elif choice == "вычитание":
                print(a - b)
            elif choice == "умножение":
                print(a * b)
            elif choice == "деление":
                print(a / b)
            elif choice == "целочисленное деление":
                print(a // b)
            elif choice == "остаток от деления":
                print(a % b)
            elif choice == "возведение в степень":
                print(a ** b)

        except ValueError:
            print("Ошибка: нужно вводить числа")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")

    elif choice == "сравнение чисел":
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print("a == b:", a == b)
            print("a != b:", a != b)
            print("a > b:", a > b)
            print("a < b:", a < b)
            print("a >= b:", a >= b)
            print("a <= b:", a <= b)
        except ValueError:
            print("Ошибка: нужно вводить числа")

    elif choice == "логические операции":
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print("a > 0 and b > 0:", a > 0 and b > 0)
            print("a > 0 or b > 0:", a > 0 or b > 0)
            print("not (a > 0):", not (a > 0))
        except ValueError:
            print("Ошибка: нужно вводить числа")

    elif choice == "проверка принадлежности":
        try:
            numbers = [1, 2, 3, 4, 5]
            x = float(input("Введите число для проверки: "))
            print("Список:", numbers)
            print("x in numbers:", x in numbers)
            print("x not in numbers:", x not in numbers)
        except ValueError:
            print("Ошибка: нужно вводить число")

    elif choice == "проверка тождественности":
        a = 10
        b = 10
        c = a
        print("a is b:", a is b)
        print("a is c:", a is c)
        print("a is not b:", a is not b)

    else:
        print("Такого варианта нет, проверьте верность написаного вами")

    print()
