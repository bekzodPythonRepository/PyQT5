from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QTabWidget")
window.resize(400, 100)
tab = QtWidgets.QTabWidget()
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 3"), "Вкладка &3")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
