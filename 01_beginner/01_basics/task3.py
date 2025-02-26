def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    try:
        x = int(input("Введите число: "))
        answer = factorial(x)
        print("Факториал числа", x, "равен", answer)
    except ValueError as e:
        print(e)