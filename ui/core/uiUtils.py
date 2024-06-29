from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


def center(self):
    # Get the primary screen's geometry
    screen_geometry = QApplication.primaryScreen().geometry()
    # Get the rectangle of the window
    window_geometry = self.frameGeometry()
    # Center the window on the screen
    window_geometry.moveCenter(screen_geometry.center())
    # Move the top-left point of the window to the top-left point of the centered geometry
    self.move(window_geometry.topLeft())


def loadUi(self, widget_file_name):
    ui_file_name = Path(widget_file_name).parent.__fspath__()
    ui_file_name += '/_.ui'
    # Load the UI file
    ui_file = QFile(ui_file_name)
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    self.ui = loader.load(ui_file, self)
    ui_file.close()
    center(self)
