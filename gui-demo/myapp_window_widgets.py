import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        #layout = QVBoxLayout()
        #widgets = [QCheckBox,
        #           QComboBox,
        #           QDateEdit,
        #           QDateTimeEdit,
        #           QDial,
        #           QDoubleSpinBox,
        #           QFontComboBox,
        #           QLCDNumber,
        #           QLabel,
        #           QLineEdit,
        #           QProgressBar,
        #           QPushButton,
        #           QRadioButton,
        #           QSlider,
        #           QSpinBox,
        #           QTimeEdit]

        #for w in widgets:
        #    layout.addWidget(w())

        #widget = QWidget()
        #widget.setLayout(layout)

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
