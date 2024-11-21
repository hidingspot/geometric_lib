# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Общее описание решения

Библиотека создана для автоматизации вычисления площади и периметра таких геометрических фигур, как *круг*, *квадрат* и *треугольник*.
Для выполнения поставленных задач были созданы функции, вычисляющие площадь и периметр названных фигур. Для каждой фигуры создана своя функция.

# Описание каждой функции с примерами вывода

1. circle.py
Функция для вычисления площади и периметра  круга.
```
import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r
```
Примеры вывода: <br>
ввод: r = 2 <br>
вывод: 
12.566370614359172
12.566370614359172

2. square.py
Функция для вычисления  площади и периметра квадрата.
```
def area(a):
    return a * a


def perimeter(a):
    return 4 * a
```
Примеры вывода: <br>
ввод: a = 5 <br>
вывод: 25 20

3. triangle.py
Функция для вычисления  площади и периметра треугольника.
```
def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c
```
Примеры вывода: <br>
ввод: a = 5, b = 3, c = 4, h = 2 <br>
вывод: 5 12 <br>

4. calculate.py
Программа выполняет вычисление заданной функции (площадь или периметр) для указанной фигуры (круг или квадрат) на основе переданных размеров фигуры.
```
import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
```
Примеры вывода: <br>
ввод: circle area 5 <br>
вывод: area of circle is 78.54 <br>
ввод: square area 4 <br>
вывод: area of square is 16
# История изменения проекта (с хешами комитов)
```
1. 8ba9aeb L-03: Circle and square added
2. d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
3. d080c78 L-04: Triangle added
4. 51c40eb L-04: Doc updated for triangle
5. d76db2a L-04: Add calculate.py
```