from PySide6.QtWidgets import QWidget, QMdiSubWindow, QMainWindow, QMdiArea
from ui.core.uiUtils import loadUi


class AppWidget(QWidget):
    def __init__(self, widget_file_name: str):
        super().__init__()
        loadUi(self, widget_file_name)


class AppMdiSubWindow(QMdiSubWindow):
    def __init__(self, widget_file_name: str):
        super().__init__()
        loadUi(self, widget_file_name)
        # uiLogin.setFixedSize(400, 300)
        actualGeo = self.ui.geometry()
        self.setGeometry(actualGeo)

