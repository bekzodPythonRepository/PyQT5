from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

window.resize(300, 50) # Минимальные размеры
window.show() # Отображаем окно
sys.exit(app.exec_())
