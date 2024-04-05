from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно
window.setWindowTitle("Вывод окна в правом нижнем углу  экрана")
window.resize(300, 100)

window.move(window.width() * -2, 0)
window.show()

desktop = QtWidgets.QApplication.desktop()
taskBarHeight = (desktop.screenGeometry().height() - desktop.availableGeometry().height())
window.move(desktop.availableGeometry().width() - window.width(), desktop.availableGeometry().height() - window.height() - taskBarHeight)
sys.exit(app.exec_())
