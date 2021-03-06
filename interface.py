import logging
import sys
from typing import Union

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLCDNumber, QPushButton, QVBoxLayout, QHBoxLayout


class SegmentalDisplay(QLCDNumber):
    def __init__(self, parent):
        super(SegmentalDisplay, self).__init__(parent)
        self.setDigitCount(2)
        self.display(2)
        self.setSegmentStyle(QLCDNumber.Flat)

    def display(self, val: Union[str, int]) -> None:
        if isinstance(val, int):
            super(SegmentalDisplay, self).display("%02d" % val)
        else:
            super(SegmentalDisplay, self).display(val)

    def increment(self):
        val = self.intValue() + 1
        if val > 99:
            logging.info("Value exceeding 99 limit")
            return
        self.display(val)

    def decrement(self):
        val = self.intValue() - 1
        if val < 0:
            logging.info("Negative value")
            return
        self.display(val)


class UpDownButtons:
    def __init__(self, parent, display):
        self.widget = QWidget(parent)
        self.layout = QVBoxLayout(self.widget)
        self.widget.setLayout(self.layout)
        self.up_button = QPushButton(parent=self.widget, text='+')
        self.down_button = QPushButton(parent=self.widget, text='-')
        self.layout.addWidget(self.up_button)
        self.layout.addWidget(self.down_button)
        self._display = display


class SegDisplayWithButtons:
    def __init__(self, parent):
        self.widget = QWidget(parent)
        self._layout = QHBoxLayout(self.widget)
        self._display = SegmentalDisplay(parent)
        self._display.setDigitCount(2)
        self.buttons = UpDownButtons(self.widget, self._display)
        self._layout.addWidget(self._display)
        self._layout.addWidget(self.buttons.widget)
        self.buttons.up_button.clicked.connect(self.increment)
        self.buttons.down_button.clicked.connect(self.decrement)

    def increment(self):
        logging.debug("Incrementing")
        self._display.increment()

    def decrement(self):
        logging.debug("Decrementing")
        self._display.decrement()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Timer and stopwatch app")
        self.resize(300, 100)
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.main_layout = QGridLayout(self)
        main_widget.setLayout(self.main_layout)
        self.hours = SegDisplayWithButtons(self)
        self.minutes = SegDisplayWithButtons(self)
        self.seconds = SegDisplayWithButtons(self)
        self.main_layout.addWidget(self.hours.widget, 0, 0)
        self.main_layout.addWidget(self.minutes.widget, 0, 1)
        self.main_layout.addWidget(self.seconds.widget, 0, 2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M', )
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
