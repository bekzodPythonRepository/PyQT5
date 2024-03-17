from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

window.setGeometry(QtCore.QRect(100, 100, 100, 70)) # Изменение одновременно положение компонента и его текущего размера
window.show() # Отображаем окно
sys.exit(app.exec_())
