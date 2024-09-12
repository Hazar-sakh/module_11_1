import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Работа с NumPy
# Создаем список с заданными параметрами
Num = []
for i in range(0, 20):
    c = []
    for j in range(1, 6):
        c.append(j)
    Num.append(c)

# Задаем массив из списка
a = np.array(Num)

# Создаем массив с рандомными целыми числами, но тем же количеством осей
b = np.random.randint(1, 20, size=(20, 5))

# Складываем значения массивов
c = a + b

# Выводим сумму чисел в массиве/в каждом столбце/каждой строке
print(f'Сумма значений массива = {c.sum()}')
print(f'Сумма значений в столбцах = {c.sum(axis=0)}')
print(f'Сумма значений в строках = {c.sum(axis=1)}')

# Выводим среднее арифметическое в массиве/в каждом столбце/каждой строке
print(f'Средне арифметическое всех значений = {c.mean()}')
print(f'Средне арифметическое в столбцах = {c.mean(axis=0)}')
print(f'Средне арифметическое в строках = {c.mean(axis=1)}')

# Выводим минимальное и максимальное значение в массиве
print(f'\nМин = {c.min()}, макс = {c.max()}')

# Выводим дисперсию для элементов массива
print(f'\nДисперсия = {c.var()}')

# Изменяем размер массива
c = np.resize(c, (3, 3))
print(f'\nНовый размер:\n{c}')


# Работа с Pandas
# Из ранее полученного массива создаем таблицу со столбцами A, B, C
tab = pd.DataFrame(c, columns=['A', 'B', 'C'])

# Выводим значения столбца B
print(f'\nПолучение значений столбца\n{tab['B']}')

# Вносим изменения в ячейку 1:1, для отличия используем неприменяемое при создании число - 99
tab.iat[1, 1] = 99
print(f'\nИзмененная таблица\n{tab}')

# Создаем файл excel без индекса (с установкой XlsxWriter)
tab.to_excel('tab.xlsx', index=False)


# Работа с Matplotlib
# Возьмем данные из ранее созданной таблицы для значения x и создадим значение y
x = list(tab['A']) + list(tab['B']) + list(tab['C'])
x.sort()
y = range(0, len(x))

# Создадим точечный график
plt.scatter(x, y)
plt.title('Ух, какая крутая табличка с точечками')
plt.show()

# Создадим линейный график
plt.plot(x, y)
plt.title('Ух, какая крутая табличка с линией')
plt.show()

# Создадим линейный график с несколькими разноцветными линиями
xd1 = list(tab['A'])
xd2 = list(tab['B'])
xd3 = list(tab['C'])
yd1 = []
for i in xd1:
    yd1.append(i * 2)
yd2 = []
for i in xd2:
    yd2.append(i / 10)
yd3 = []
for i in xd3:
    yd3.append(1 - i * 3)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xd1, yd1, color='tab:blue')
ax.plot(xd2, yd2, color='tab:red')
ax.plot(xd3, yd3, color='tab:green')
plt.title('Битва Квай-Гона Джинна и Оби-Вана Кеноби против Дарта Мола')
plt.show()

# Создадим круговой график
plt.pie(x, labels=x)
plt.title('Ух, кружочек разноцветный')
plt.show()
