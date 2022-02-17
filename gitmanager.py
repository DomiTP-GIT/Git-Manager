# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path

import qdarkstyle
from PySide6.QtCore import Slot, QThreadPool, QSize
from PySide6.QtGui import QIcon, QActionGroup, QKeySequence, QMovie
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QListWidgetItem, QFileDialog

from Ui_main import Ui_gitManager


class GitManager(QMainWindow):
    def __init__(self):
        super(GitManager, self).__init__()
        self.window = Ui_gitManager()
        self.window.setupUi(self)

        self.home = str(Path.home())
        self.ruta_buscar = self.home

        self.thread_manager = QThreadPool()

        self.window.projects.setStyleSheet("QListView::item"
                                           "{"
                                           "padding : 10px;"
                                           "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                           "}"
                                           "QListView::hover"
                                           "{"
                                           "color : black"
                                           "}"
                                           )

        # Carga la configuración
        self.config()

        # Carga los proyectos
        self.thread_load_projects()

    # Configura inicialmente la ventana y los componentes que tiene
    def config(self):
        self.setWindowTitle("Git Manager")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/git-manager.png")))

        self.window.projects.setAlternatingRowColors(True)
        self.window.projects.setDragDropMode(QAbstractItemView.InternalMove)

        self.window.btnRuta.clicked.connect(self.get_route)
        self.window.btnUpdate.clicked.connect(self.thread_load_projects)
        self.window.rutaEdit.setText(self.ruta_buscar)
        self.window.btnUpdate.setShortcut(QKeySequence("F5"))
        self.window.btnUpdate.setShortcut(QKeySequence("Ctrl+R"))

        loadingGifMovie = QMovie(os.path.join(os.path.dirname(__file__), "resources/loading.gif"))
        loadingGifMovie.setScaledSize(QSize(20, 20))
        self.window.loadingGif.setMovie(loadingGifMovie)
        loadingGifMovie.start()
        self.window.loadingGif.setHidden(True)

        # Cambio de modo interfaz
        modo_claro_oscuro = QActionGroup(self)
        modo_claro_oscuro.setExclusive(True)
        modo_claro_oscuro.addAction(self.window.actionClaro)
        modo_claro_oscuro.addAction(self.window.actionOscuro)
        self.window.actionClaro.setChecked(True)
        self.window.actionClaro.triggered.connect(self.cambiar_claro)
        self.window.actionOscuro.triggered.connect(self.cambiar_oscuro)

    @Slot()
    def load_projects(self):
        self.window.loadingGif.setHidden(False)
        self.window.projects.clear()
        for root, subdirs, files in os.walk(self.ruta_buscar):
            for d in subdirs:
                if os.access(root, os.R_OK):
                    if d == ".git":
                        folder_name = root.split(os.sep)[-1]
                        item = QListWidgetItem()
                        item.setText(folder_name)
                        item.setToolTip(root)
                        self.window.projects.addItem(item)
                else:
                    print(d + " No permission")
        self.window.loadingGif.setHidden(True)

    @Slot()
    def thread_load_projects(self):
        self.thread_manager.start(self.load_projects)

    def get_route(self):
        nueva_ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", self.home)
        if nueva_ruta:
            self.ruta_buscar = nueva_ruta
            self.window.rutaEdit.setText(nueva_ruta)
            self.thread_load_projects()

    def set_route(self, text):
        self.ruta_buscar = text
        # Aplicar el estilo a los QListView

    def cambiar_claro(self):
        self.setStyleSheet("")
        self.window.projects.setStyleSheet("QListView::item"
                                           "{"
                                           "padding : 10px;"
                                           "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                           "color : black"
                                           "}"
                                           "QListView::hover"
                                           "{"
                                           "color : black"
                                           "}"
                                           "QListItemView"
                                           "{"
                                           "color : black"
                                           "}"
                                           )

    def cambiar_oscuro(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.window.projects.setStyleSheet("QListView::item"
                                           "{"
                                           "padding : 10px;"
                                           "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                           "}"
                                           "QListView::hover"
                                           "{"
                                           "color : white"
                                           "}"
                                           )


if __name__ == "__main__":
    app = QApplication([])
    widget = GitManager()
    widget.show()
    sys.exit(app.exec())
