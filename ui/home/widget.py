from PySide6.QtWidgets import (QMainWindow, QMdiArea)

from ui.home.mainWindow import Ui_MainWindow
from ui.login.widget import LoginUi


class UiMainWindowExt(Ui_MainWindow):

    def __init__(self, win: QMainWindow):
        UiMainWindowExt.mdi = QMdiArea()
        self.win = win

    def setupUi(self):
        super().setupUi(self.win)
        self.win.setCentralWidget(UiMainWindowExt.mdi)
        UiMainWindowExt.openLoginWin()
        self.actionLogin.triggered.connect(UiMainWindowExt.openLoginWin)

    # @Slot()
    @staticmethod
    def openLoginWin():
        uiLogin = LoginUi()
        uiLogin.openAsNonCloseableModal(UiMainWindowExt.mdi)


class HomeUi:
    def __init__(self):
        self.win = QMainWindow()
        ui = UiMainWindowExt(self.win)
        ui.setupUi()

    def show(self):
        self.win.show()
