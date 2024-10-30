from PySide6.QtWidgets import QMessageBox, QStatusBar

statusBar: QStatusBar = None


def message(msg, title="message", parent=None):
    dlg = QMessageBox(parent=parent)
    dlg.setWindowTitle(title)
    dlg.setText(msg)
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.show()
