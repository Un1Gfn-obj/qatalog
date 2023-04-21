#!/bin/python3

import sys
import qywidget
import PySide6

def main():

    app = PySide6.QtWidgets.QApplication([])

    w = qywidget.QyWidget()
    # w.resize(800, 600)
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    main()

