import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui.home.widget import HomeUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = HomeUi()
    ui.show()
    sys.exit(app.exec())
