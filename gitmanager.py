# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path

from PySide6.QtGui import QIcon, Qt, QActionGroup
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QListWidgetItem, QFileDialog
import qdarkstyle


class GitManager(QMainWindow):
    def __init__(self):
        super(GitManager, self).__init__()
        self.window = self.load_ui()

        self.home = str(Path.home())
        self.ruta_buscar = self.home

        # Carga la configuración
        self.config()

        # Inicia la ventana (Iniciará vacía y cuando se carguen los proyectos se iniciará completamente)
        self.window.show()

        # Carga los proyectos
        self.load_projects()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "main.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        return loader.load(path, self)
        # ui_file.close()

    def config(self):
        self.window.setWindowTitle("Git Manager")
        self.window.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/githubmanager.png")))
        self.window.projects.setStyleSheet("QListView::item"
                                           "{"
                                           "padding : 10px;"
                                           "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                           "}"
                                           )
        self.window.projects.setAlternatingRowColors(True)
        self.window.projects.setDragDropMode(QAbstractItemView.InternalMove)
        self.window.btnRuta.clicked.connect(self.get_route)
        self.window.rutaEdit.setText(self.ruta_buscar)
        self.window.btn_update.clicked.connect(self.load_projects)

        # Cambio de modo interfaz
        modo_claro_oscuro = QActionGroup(self)
        modo_claro_oscuro.setExclusive(True)
        modo_claro_oscuro.addAction(self.window.actionClaro)
        modo_claro_oscuro.addAction(self.window.actionOscuro)
        self.window.actionClaro.setChecked(True)
        self.window.actionClaro.triggered.connect(self.cambiar_claro)
        self.window.actionOscuro.triggered.connect(self.cambiar_oscuro)

    def load_projects(self):
        for root, subdirs, files in os.walk(self.ruta_buscar):
            for d in subdirs:
                if os.access(root, os.R_OK):
                    if d == ".git":
                        folder_name = root.split("\\")[-1]
                        item = QListWidgetItem()
                        item.setText(folder_name)
                        item.setToolTip(root)
                        self.window.projects.addItem(item)
                else:
                    print(d + " No permission")

    def get_route(self):
        nueva_ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", self.home)
        if nueva_ruta:
            self.ruta_buscar = nueva_ruta
            self.window.rutaEdit.setText(nueva_ruta)
            self.load_projects()

    def set_route(self, text):
        self.ruta_buscar = text

    def cambiar_claro(self):
        self.window.setStyleSheet("")

    def cambiar_oscuro(self):
        self.window.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())


if __name__ == "__main__":
    app = QApplication([])
    widget = GitManager()
    sys.exit(app.exec())
