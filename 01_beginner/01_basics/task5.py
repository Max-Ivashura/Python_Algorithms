def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    try:
        number = int(input("Введите число: "))
        multiplication_table(number)
    except ValueError:
        print("Ошибка: введите целое число.")