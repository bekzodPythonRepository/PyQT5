from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
s1 = QtCore.QSize(50, 20)
s2 = s1.transposed()
print(s1, s2) # PyQt5.QtCore.QSize(50, 20) PyQt5.QtCore.QSize(20, 50)
