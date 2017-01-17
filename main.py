import sys

from PyQt5.QtWidgets import QApplication

from RTH.views.main_window import MainUI


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('fusion')
    main_ui = MainUI()
    sys.exit(app.exec())
