from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect()
r.setLeft(10)
r.setTop(55)
print(r) # PyQt5.QtCore.QRect(10, 55, -10, -55)
r.setX(12)
r.setY(81)
print(r) # PyQt5.QtCore.QRect(12, 81, -12, -81)
