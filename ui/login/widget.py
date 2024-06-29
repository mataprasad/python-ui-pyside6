import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QVBoxLayout, QDialog, QMdiArea)

from ui.core.appWidget import AppMdiSubWindow
from ui.core.uiUtils import center


class LoginUi(AppMdiSubWindow):

    def __init__(self):
        super().__init__(__file__)

        # Access widgets and connect signals
        # self.setWindowState(Qt.WindowState.WindowActive)
        # self.ui.geometry()
        self.ui.btnLogin.clicked.connect(self.on_btnLogin_clicked)
        self.ui.btnExit.clicked.connect(self.on_btnExit_clicked)

    @Slot()
    def on_btnExit_clicked(self):
        sys.exit()

    @Slot()
    def on_btnLogin_clicked(self):
        self.dialog.close()
        print("Hello World!!!")

    def openAsNonCloseableModal(self, mdi: QMdiArea):
        self.dialog = QDialog(mdi)
        self.dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.dialog.setWindowTitle('Modal Dialog Example')
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.dialog.setLayout(layout)
        self.dialog.setGeometry(self.ui.geometry())
        center(self.dialog)
        self.dialog.exec()
