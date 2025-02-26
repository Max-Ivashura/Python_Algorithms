def is_prime(n):
    # Проверяем, что число больше 1
    if n <= 1:
        return False
    # Проверяем делители от 2 до корня числа
    for i in range(2, int(n**0.5) + 1):  # Используем sqrt(n) для оптимизации
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    try:
        num = int(input("Введите число: "))
        if is_prime(num):
            print("Число простое")
        else:
            print("Число не простое")
    except ValueError:
        print("Ошибка: введите целое число.")