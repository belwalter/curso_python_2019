#!/usr/bin/python3
import sys
#import menu_muestra
#import cargar_museo
#import visor_mapa
#from funciones_mongo import lista_museos

from segunda import ventana_secundaria

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("principal.ui", self)
        self.show()
        self.boton.clicked.connect(self.completar)
        #self.agregar_museo.clicked.connect(self.agregar_museo_)

    def completar(self):
        self.text.setText("hola mundo")
        menu = ventana_secundaria()
        menu.show()
        menu.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
