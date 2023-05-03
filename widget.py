#!/dev/null

from PySide6 import (
    QtWidgets,
    QtCore,
)

import qyalash.widget
import pdf.widget

class Widget(QtWidgets.QWidget):

    @QtCore.Slot()
    def general(self, x):
        # if self.l2w:
        #     self.l2w.close()
        #     self.l2w = None
        # else:
        self.l2w = x.Widget()
        self.l2w.show()

    def b(self, widget, name, tooltip):
        button = QtWidgets.QPushButton(name)
        button.setFlat(False)
        button.clicked.connect(lambda : self.general(widget))
        if tooltip:
            button.setToolTip(tooltip)
        self.layout.addWidget(button)
        return button

    def __init__(self):
        super().__init__()
        self.l2w = None
        self.layout = QtWidgets.QVBoxLayout(self)
        self.b(qyalash.widget, "qyalash", "clash process manager (Linux only)")
        self.b(pdf.widget,     "pdf",     None)

