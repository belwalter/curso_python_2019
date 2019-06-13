from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class ventana_secundaria(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("secundaria.ui", self)
        self.texto.setText("HOLA")
