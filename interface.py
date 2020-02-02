import sys

from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QLCDNumber


class Numerical(QLCDNumber):
    def __init__(self, parent):
        super(Numerical, self).__init__(parent)
        self.setSegmentStyle(QLCDNumber.Filled)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Timer and stopwatch app")
        self.resize(400, 500)
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.main_layout = QGridLayout(self)
        main_widget.setLayout(self.main_layout)
        self.numerical = Numerical(self)
        self.main_layout.addWidget(self.numerical, 0, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())