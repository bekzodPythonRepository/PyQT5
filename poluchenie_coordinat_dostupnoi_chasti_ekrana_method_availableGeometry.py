from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

desktop = QtWidgets.QApplication.desktop()
rect = desktop.availableGeometry()
print(rect.left(),rect.top()) # 70 32
print(rect.width(), rect.height()) # 1850 1048

window.show() # Отображаем окно
sys.exit(app.exec_())
