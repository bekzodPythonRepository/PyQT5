from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
s1 = QtCore.QSize(50, 20)
s2 = QtCore.QSize(10, 5)
print(s1 + s2) # PyQt5.QtCore.QSize(60, 25)
print(s1 - s2) # PyQt5.QtCore.QSize(40, 15)
print(s1 * 2.5) # PyQt5.QtCore.QSize(125, 50)
print(s1 / 2) # PyQt5.QtCore.QSize(25, 10)
print(s1 == s2) # False
print(s1 != s2) # True
