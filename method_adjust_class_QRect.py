from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

r = QtCore.QRect(0, 0, 400, 300)
r.adjust(10, 5, 10, 5)
print(r) # PyQt5.QtCore.QRect(10, 5, 400, 300)
