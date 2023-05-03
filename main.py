#!/usr/bin/env python3

import sys
import PySide6

import widget

def main():
    app = PySide6.QtWidgets.QApplication([])
    w = widget.Widget()
    w.show()
    # w.resize(800, 600)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

