import sys

from PyQt5.QtWidgets import QApplication

from RTH.views.main_window import MainUI


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName('SlowSoft')
    app.setApplicationName('RimWorldTranslationHelper')
    main_ui = MainUI()
    sys.exit(app.exec())
