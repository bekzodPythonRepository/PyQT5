from PyQt5 import QtCore, QtWidgets
import sys


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("Всплывающие подсказки")
window.resize(300, 70)
button = QtWidgets.QPushButton("Закрыть окно")
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip("Эта всплывающая подсказка для кнопки")
button.setToolTipDuration(3000)
window.setToolTip("Эта всплывающаяподсказка для окна")
window.setToolTipDuration(5000)
button.setWhatsThis("Эта справка для кнопки")
window.setWhatsThis("Эта справка для окна")
button.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(app.exec_())
