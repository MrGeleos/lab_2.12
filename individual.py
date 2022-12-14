#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Объявите функцию, которая вычисляет периметр многоугольника и возвращает
вычисленное значение. Длины сторон многоугольника передаются в виде коллекции (списка
или кортежа). Определите декоратор для этой функции, который выводит на экран
сообщение: «Периметр фигуры равен = <число>». Примените декоратор к функции и
вызовите декорированную функцию.
"""


def perimetr(fan):
    def help_pr(spisok):
        s = fan(spisok)
        print(f"Периметр фигуры равен = {s}")
        return s

    return help_pr


@perimetr
def get_pr(spisok):
    return sum(spisok)


if __name__ == '__main__':
    a = [2, 5, 2, 7, 5]
    get_pr(a)
