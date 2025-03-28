from PyQt5 import QtCore, QtWidgets
import time

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Использование QTimer.singleShot")
        self.resize(200, 100)
        self.label = QtWidgets.QLabel("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button1 = QtWidgets.QPushButton("Запустить")
        self.button2 = QtWidgets.QPushButton("Остановить")
        self.button2.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)

    def on_clicked_button1(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)
        self.on_timeout() # Запускаем обновление времени
        QtCore.QTimer.singleShot(1000, QtWidgets.qApp.quit)# Закрываем окно

    def on_clicked_button2(self):
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def on_timeout(self):
        self.label.setText(time.strftime("%H:%M:%S"))
        QtCore.QTimer.singleShot(1000, self.on_timeout)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
