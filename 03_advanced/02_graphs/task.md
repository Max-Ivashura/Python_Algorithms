# Graphs Tasks

Добро пожаловать в раздел графов! Здесь вы найдете задачи, которые помогут вам углубить свои знания о графовых алгоритмах.

## Список задач

### 1. Обход графа в глубину (DFS)
**Описание:**  
Реализуйте алгоритм обхода графа в глубину.  

**Требования:**  
- Создайте граф как словарь смежности.
- Напишите функцию для выполнения обхода в глубину.
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
['A', 'B', 'D', 'E', 'F', 'C']
~~~

**Файл решения:** task1.py

---

### 2. Обход графа в ширину (BFS)
**Описание:**  
Реализуйте алгоритм обхода графа в ширину.  

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

**Файл решения:** task2.py

---

### 3. Кратчайший путь (Dijkstra)
**Описание:**  
Найдите кратчайший путь между двумя вершинами графа с использованием алгоритма Дейкстры.  

**Требования:**  
- Создайте взвешенный граф.
- Напишите функцию для выполнения алгоритма Дейкстры.
- Выведите кратчайший путь.

**Пример:**  
Граф:  
~~~
{
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
~~~
Вывод:  
~~~
Кратчайший путь от A до D: ['A', 'B', 'C', 'D'], Длина: 4
~~~

**Файл решения:** task3.py

---

### 4. Минимальное остовное дерево (Kruskal)
**Описание:**  
Найдите минимальное остовное дерево графа с использованием алгоритма Крускала.  

**Требования:**  
- Создайте взвешенный граф.
- Напишите функцию для выполнения алгоритма Крускала.
- Выведите ребра минимального остовного дерева.

**Файл решения:** task4.py

---

### 5. Циклы в графе
**Описание:**  
Проверьте, содержит ли граф циклы с использованием обхода в глубину.  

**Требования:**  
- Создайте граф как словарь смежности.
- Напишите функцию для проверки наличия циклов.
- Выведите "Содержит циклы" или "Не содержит циклов".

**Файл решения:** task5.py