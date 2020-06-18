import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar
from PyQt5.QtWidgets import QAction, QStatusBar, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        # disable right clicking on the toolbar to prevent user from hiding it
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("/home/ychoon/python-gui/gui-demo/fugue-icons-3.5.6/icons/calendar.png"), "My button", self)
        button_action.setStatusTip("This is my button.")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("/home/ychoon/python-gui/gui-demo/fugue-icons-3.5.6/icons/bug.png"), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        toolbar.addSeparator()

        button_action3 = QAction(QIcon("/home/ychoon/python-gui/gui-demo/fugue-icons-3.5.6/bonus/icons-32/cross.png"),"Quit", self)
        button_action3.triggered.connect(app.quit)
        toolbar.addAction(button_action3)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("clicked", s)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
