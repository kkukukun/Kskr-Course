# * - coding: utf-8 - *-
# подключение библиотеки tkinter
from tkinter import *
# импорт математической библиотеки
from math import *
import numpy as np
import matplotlib.pyplot as plt


# описание функции
def du(x, y):
    return y * np.sin(e ** x)


def rk(x_0, y_0, x_k, n_1):
    # разбиение отрезка на точки
    h = (x_k - x_0) / n_1
    # метод рунге-кутта
    for i in range(0, n_1):
        k1 = h * du(x_0, y_0)
        k2 = h * du(x_0 + h / 2, y_0 + k1 / 2)
        k3 = h * du(x_0 + h / 2, y_0 + k2 / 2)
        k4 = h * du(x_0 + h, y_0 + k3)
        y1 = y_0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_0 = x_0 + h
        y_0 = y1
    return y1


def calc_y():
    # начальные условия
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    # конечная точка
    xk = float(xk_entry.get())
    # число разбиений
    n = int(n_entry.get())
    try:
        y = "%.3f" % rk(x0, y0, xk, n)
    except:
        y = "?"
    y2_label.configure(text=y)


def graf():
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    # конечная точка
    xk = float(xk_entry.get())
    # число разбиений
    n = int(n_entry.get())
    x = np.linspace(x0, xk, n)
    y = rk(x0, y0, xk, n)
    f = y * np.sin(e ** x)
    plt.title("Линейная зависимость f(x)")
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.plot(x, f)  # построение графика
    plt.show()


# создание экземпляра класса Tk, отвечающего за создание окон
root = Tk()
# определение заголовка окна
root.title("Курсовой проект")
frame = Frame(root)
frame.pack()
t1_label = Label(frame, bg='tan', text="Численное решение дифференциального уравнения первого порядка", font='arial 12')
t1_label.grid(row=0, column=0, columnspan=5, padx=25, pady=5)
# создание окна ввода величины начального значения числа X
x0_entry = Entry(frame, width=10)
x0_entry.grid(row=1, column=2, pady=5)
x0_lebel = Label(frame, text="Начальное значение X: ")
x0_lebel.grid(row=1, column=1, pady=5)
# создание окна ввода величины начального значения числа Y
y0_entry = Entry(frame, width=10)
y0_entry.grid(row=2, column=2, pady=5)
y0_lebel = Label(frame, text="Начальное значение Y: ")
y0_lebel.grid(row=2, column=1, pady=5)
# создание окна ввода величины конечной точки
xk_entry = Entry(frame, width=10)
xk_entry.grid(row=1, column=4, pady=5)
xk_lebel = Label(frame, text="Конечное значение Х: ")
xk_lebel.grid(row=1, column=3, pady=5)
# создание окна ввода величины точности интегрирования)
n_entry = Entry(frame, width=10)
n_entry.grid(row=2, column=4, pady=5)
n_lebel = Label(frame, text="Число разбиений: ")
n_lebel.grid(row=2, column=3, pady=5)
# создание поля вывода ответа (метод рунге-кутта)
y2_label = Label(frame, text="?")
y2_label.grid(row=3, column=1, padx=5, pady=5)
y2_lebel = Label(frame, text="Метод Рунге-Кутта 4го порядка: ")
y2_lebel.grid(row=3, column=0, padx=5, pady=5)
# создание кнопки вычисления значения интеграла
graf_button = Button(frame, bg='coral', text="График", width=10, command=graf)
graf_button.grid(row=3, column=2, padx=5, pady=5)
# Кнопка для чтения примера из файла
read_button = Button(frame, bg='coral', text="Пример", width=10, command=calc_y)
read_button.grid(row=3, column=5, padx=5, pady=5)
# создание кнопки закрытия приложения
eval_button = Button(frame, bg='coral', text="Вычислить", width=10, command=calc_y)
eval_button.grid(row=3, column=3, padx=5, pady=5)
exit_button = Button(frame, bg='coral', text="Выход", width=10, command=root.destroy)
exit_button.grid(row=3, column=4, padx=5, pady=5)
# непосредственное создание окна
root.mainloop()
