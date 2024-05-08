from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
s1 = QtCore.QSize(50, 20)
s2 = s1.scaled(70, 60, QtCore.Qt.IgnoreAspectRatio)
print(s1, s2) # PyQt5.QtCore.QSize(50, 20) PyQt5.QtCore.QSize(70, 60)
