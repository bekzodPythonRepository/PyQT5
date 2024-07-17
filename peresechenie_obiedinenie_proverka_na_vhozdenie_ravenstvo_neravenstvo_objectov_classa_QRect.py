from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

r1 = QtCore.QRect(0, 0, 20, 20)
r2 = QtCore.QRect(10, 10, 20, 20)

# пересечение:
print(r1 & r2) # PyQt5.QtCore.QRect(10, 10, 10, 10)

# обьединение:
print(r1 | r2) # PyQt5.QtCore.QRect(0, 0, 30, 30)

#вхождение:
print(r1 in r2) # False
print(r1 in QtCore.QRect(0, 0, 30, 30)) # True

#равенство и неравенство
print(r1 == r2) # False
print(r1 != r2) # True
