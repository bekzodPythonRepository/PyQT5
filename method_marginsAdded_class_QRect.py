from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r1 = QtCore.QRect(10, 15, 400, 300)
m = QtCore.QMargins(5, 2, 5, 2)
r2 = r1.marginsAdded(m)
print(r2) # PyQt5.QtCore.QRect(5, 13, 410, 304)
print(r1) # PyQt5.QtCore.QRect(10, 15, 400, 300)
