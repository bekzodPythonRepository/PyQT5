from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
s = QtCore.QSize(50, 20)
s.transpose()
print(s) # PyQt5.QtCore.QSize(20, 50)
