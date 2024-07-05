from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(0, 0, 400, 300)
print(r.contains(0, 10), r.contains(0, 10, True)) # True False
r1 = QtCore.QRect(0, 0, 400, 300)
print(r.contains(QtCore.QRect(0, 0, 20, 5))) # True
print(r.contains(QtCore.QRect(0, 0, 20, 5), True)) # False
