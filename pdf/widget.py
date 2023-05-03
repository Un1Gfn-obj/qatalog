import psutil
from PySide6 import (
    QtCore,
    QtWidgets,
    QtGui,
)

TE = """\
[rotate]
qpdf IN.pdf IN-90.pdf --rotate=90

[2up stack vertically]
pdfjam --paper a3paper --nup 1x2 IN.pdf
"""

class Widget(QtWidgets.QTextEdit):

    def __init__(self):
        super().__init__()
        self.setAcceptRichText(False)
        self.setPlainText(TE)
        self.setReadOnly(True)
