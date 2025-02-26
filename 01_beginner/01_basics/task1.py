def sum(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    try:
        n1 = int(input('Введите первое число: '))
        n2 = int(input('Введите второе число: '))
        print("Сумма:", sum(n1, n2))
    except ValueError:
        print("Ошибка: введите целые числа.")
