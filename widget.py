#!/dev/null

from PySide6 import (
    QtWidgets,
    QtCore,
)

import qyalash.widget

class Widget(QtWidgets.QWidget):

    @QtCore.Slot()
    def yoi8qm(self):
        # if self.l2w:
        #     self.l2w.close()
        #     self.l2w = None
        # else:
            self.l2w = qyalash.widget.Widget()
            self.l2w.show()

    # @QtCore.Slot()
    # def vd5myn(self):
    #     self.l2w = pdf.widget.Widget()
    #     self.l2w.show()

    def b(self, function, name, tooltip):
        button = QtWidgets.QPushButton(name)
        button.setFlat(False)
        button.clicked.connect(function)
        if tooltip:
            button.setToolTip(tooltip)
        self.layout.addWidget(button)
        return button

    def __init__(self):
        super().__init__()
        self.l2w = None
        self.layout = QtWidgets.QVBoxLayout(self)
        self.b(self.yoi8qm, "qyalash", "clash process manager (Linux only)")
        # self.b(self.vd5myn, "pdf", None)

