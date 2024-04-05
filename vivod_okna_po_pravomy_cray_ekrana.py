from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно
window.setWindowTitle("Вывод окна по правому краю экрана")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()

desktop = QtWidgets.QApplication.desktop()
x = desktop.width() - window.frameSize().width()
window.move(x, 0)
sys.exit(app.exec_())
