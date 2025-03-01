# Data Structures Tasks

Добро пожаловать в раздел структур данных! Здесь вы найдете задачи, которые помогут вам освоить использование различных структур данных, таких как стеки, очереди, хэш-таблицы и деревья.

## Список задач

### 1. Стек
**Описание:**  
Реализуйте стек с использованием списка.  

**Требования:**  
- Создайте класс `Stack` с методами `push`, `pop`, `peek` и `is_empty`.
- Протестируйте работу стека.

**Файл решения:** task1.py

---

### 2. Очередь
**Описание:**  
Реализуйте очередь с использованием списка.  

**Требования:**  
- Создайте класс `Queue` с методами `enqueue`, `dequeue`, `peek` и `is_empty`.
- Протестируйте работу очереди.

**Файл решения:** task2.py

---

### 3. Хэш-таблица
**Описание:**  
Создайте свою реализацию хэш-таблицы с разрешением коллизий.  

**Требования:**  
- Реализуйте класс `HashTable` с методами `insert`, `get` и `delete`.
- Протестируйте работу хэш-таблицы.

**Файл решения:** task3.py

---

### 4. Двоичное дерево
**Описание:**  
Реализуйте двоичное дерево с методами добавления и удаления элементов.  

**Требования:**  
- Создайте класс `BinaryTree` с методами `insert`, `search` и `delete`.
- Протестируйте работу дерева.

**Файл решения:** task4.py

---

### 5. Граф
**Описание:**  
Создайте граф и реализуйте его обход в ширину (BFS).  

**Требования:**  
- Создайте граф как словарь смежности.
- Напишите функцию для выполнения обхода в ширину.
- Выведите порядок обхода вершин.

**Пример:**  
Граф:  
~~~
{
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
~~~
Вывод:  
~~~
['A', 'B', 'C', 'D', 'E', 'F']
~~~

**Файл решения:** task5.py