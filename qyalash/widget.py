import random
import psutil
from PySide6 import QtCore, QtWidgets, QtGui

from . import util

class Widget(QtWidgets.QWidget):

    def mkbutton(self, name, **kwargs):

        button = QtWidgets.QPushButton(name)
        for k, v in kwargs.items():
            if k == "tooltip":
                button.setToolTip(v)
            elif k == "slot":
                if v is None:
                    button.setFlat(True)
                else:
                    button.clicked.connect(v)
        self.layout.addWidget(button)
        return button

    def __init__(self):

        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.text)

        self.mkbutton("?", slot=self.a91t47)
        self.mkbutton("update", slot=None)
        self.br = self.mkbutton("run",    slot=self.wu1vzk)
        self.bk = self.mkbutton("kill",   slot=self.ncs3u8, tooltip="terminate clash, keep log")
        if util.running():
            self.br.setFlat(True)
            self.bk.setFlat(False)
        else:
            self.br.setFlat(False)
            self.bk.setFlat(True)
        # self.bp = self.mkbutton("purge",  slot=None,        tooltip="terminate clash, clear logs")
        self.mkbutton("log",    slot=self.kx26k8, tooltip="view clash log")

    @QtCore.Slot()
    def a91t47(self):
        self.text.setText(random.choice(self.hello))

    @QtCore.Slot()
    def wu1vzk(self):
        if util.running():
            QtWidgets.QMessageBox.critical(self, " ", "already running")
        else:
            util.run()
            QtWidgets.QMessageBox.information(self, " ", "OK")
            self.br.setFlat(True)
            self.bk.setFlat(False)

    @QtCore.Slot()
    def kx26k8(self):
        util.log()

    @QtCore.Slot()
    def ncs3u8(self):
        util.kill()
        QtWidgets.QMessageBox.information(self, " ", "terminated")
        self.br.setFlat(False)
        self.bk.setFlat(True)
