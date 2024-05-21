from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
s = QtCore.QSize(50, 20)
print(s.expandedTo(QtCore.QSize(400, 5))) # PyQt5.QtCore.QSize(400, 20)
print(s.expandedTo(QtCore.QSize(40, 50))) # PyQt5.QtCore.QSize(50, 50)
