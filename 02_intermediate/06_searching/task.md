# Searching Tasks

Добро пожаловать в раздел поиска! Здесь вы найдете задачи, которые помогут вам освоить различные алгоритмы поиска.

## Список задач

### 1. Линейный поиск
**Описание:**  
Реализуйте алгоритм линейного поиска для поиска элемента в списке.  

**Требования:**  
- Создайте список чисел.
- Напишите функцию для выполнения линейного поиска.
- Выведите индекс элемента или сообщение "Элемент не найден".

**Пример:**  
Ввод:  
~~~
Список: [2, 4, 6, 8, 10], Элемент: 6
~~~
Вывод:  
~~~
Индекс элемента: 2
~~~

**Файл решения:** task1.py

---

### 2. Бинарный поиск
**Описание:**  
Реализуйте алгоритм бинарного поиска для поиска элемента в отсортированном списке.  

**Требования:**  
- Создайте отсортированный список чисел.
- Напишите функцию для выполнения бинарного поиска.
- Выведите индекс элемента или сообщение "Элемент не найден".

**Пример:**  
Ввод:  
~~~
Список: [2, 4, 6, 8, 10], Элемент: 6
~~~
Вывод:  
~~~
Индекс элемента: 2
~~~

**Файл решения:** task2.py

---

### 3. Поиск подстроки
**Описание:**  
Напишите функцию для поиска подстроки в строке с использованием алгоритма Кнута-Морриса-Пратта (KMP).  

**Требования:**  
- Функция должна принимать две строки: основную строку и подстроку.
- Выведите индексы всех вхождений подстроки.

**Пример:**  
Ввод:  
~~~
Строка: "ababcababa", Подстрока: "aba"
~~~
Вывод:  
~~~
[0, 4, 6]
~~~

**Файл решения:** task3.py

---

### 4. Поиск минимума/максимума
**Описание:**  
Напишите функцию для поиска минимального и максимального элементов в списке.  

**Требования:**  
- Создайте список чисел.
- Найдите минимальный и максимальный элементы.
- Выведите результат.

**Пример:**  
Ввод:  
~~~
[5, 3, 8, 6, 2]
~~~
Вывод:  
~~~
Минимум: 2, Максимум: 8
~~~

**Файл решения:** task4.py

---

### 5. Поиск в матрице
**Описание:**  
Напишите функцию для поиска элемента в отсортированной матрице.  

**Требования:**  
- Матрица должна быть отсортирована по строкам и столбцам.
- Напишите функцию для поиска элемента.
- Выведите координаты элемента или сообщение "Элемент не найден".

**Пример:**  
Ввод:  
~~~
Матрица:
[
  [1, 3, 5],
  [7, 9, 11],
  [13, 15, 17]
]
Элемент: 9
~~~
Вывод:  
~~~
Координаты: (1, 1)
~~~

**Файл решения:** task5.py