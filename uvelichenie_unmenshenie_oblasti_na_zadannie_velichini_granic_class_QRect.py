from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
m = QtCore.QMargins(5, 15, 5, 15)
print(r + m) # PyQt5.QtCore.QRect(5, 0, 410, 330)
print(r - m) # PyQt5.QtCore.QRect(15, 30, 390, 270)
