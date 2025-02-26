def even_numbers_generator(start, finish, step):
    return [i for i in range(start, finish + 1, step)]

if __name__ == '__main__':
    even_numbers = even_numbers_generator(0, 20, 2)
    print(even_numbers)