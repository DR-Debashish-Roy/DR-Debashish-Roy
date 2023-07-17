from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
from PyQt5 import QtCore, QtWidgets
import sys


class MDIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self._mdiarea = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New Customer")
        file.triggered[QAction].connect(self.windowTrig)
        self.setWindowTitle("RMO Tradeshow System")
        self.showMaximized()

    def windowTrig(self, p):
        if p.text() == "New Customer":
            sub = QMdiSubWindow()
            sub.setWindowTitle("Add New Customer")
            sub.setFixedWidth(600)
            sub.setFixedHeight(600)

            sub.show()
            sub.setProperty("center", True)
            center = self._mdiarea.viewport().rect().center()
            geo = sub.geometry()
            geo.moveCenter(center)
            sub.setGeometry(geo)


app = QApplication(sys.argv)
mdi = MDIWindow()
mdi.show()
app.exec_()
