# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path

import qdarktheme
from PySide6.QtCore import Slot, QThreadPool, QSize
from PySide6.QtGui import QIcon, QActionGroup, QKeySequence, QMovie
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QListWidgetItem, QFileDialog, QWidget

from Ui_main import Ui_gitManager
from clone import Clone
from project import Project


class GitManager(QMainWindow):
    def __init__(self):
        super(GitManager, self).__init__()
        self.ui = Ui_gitManager()
        self.ui.setupUi(self)

        self.home = str(Path.home())
        self.ruta_buscar = self.home

        self.thread_manager = QThreadPool()
        self.clonar = QWidget()
        self.proyecto = QWidget()

        # Carga la configuración
        self.config()

        # Carga los proyectos
        self.thread_load_projects()

    # Configura inicialmente la ventana y los componentes que tiene
    def config(self):
        self.setWindowTitle("Git Manager")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/git-manager.png")))

        self.ui.projects.setAlternatingRowColors(True)
        self.ui.projects.setDragDropMode(QAbstractItemView.InternalMove)

        self.ui.projects.setStyleSheet("QListView::item"
                                       "{"
                                       "padding : 10px;"
                                       "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                       "}"
                                       )

        self.ui.btnRuta.clicked.connect(self.get_route)
        self.ui.btnUpdate.clicked.connect(self.thread_load_projects)
        self.ui.btnClonar.clicked.connect(self.clone)
        self.ui.rutaEdit.setText(self.ruta_buscar)
        self.ui.btnUpdate.setShortcut(QKeySequence("F5"))
        self.ui.btnUpdate.setShortcut(QKeySequence("Ctrl+R"))

        loadingGifMovie = QMovie(os.path.join(os.path.dirname(__file__), "resources/loading.gif"))
        loadingGifMovie.setScaledSize(QSize(20, 20))
        self.ui.loadingGif.setMovie(loadingGifMovie)
        loadingGifMovie.start()
        self.ui.loadingGif.setHidden(True)

        # Cambio de modo interfaz
        modo_claro_oscuro = QActionGroup(self)
        modo_claro_oscuro.setExclusive(True)
        modo_claro_oscuro.addAction(self.ui.actionClaro)
        modo_claro_oscuro.addAction(self.ui.actionOscuro)
        self.ui.actionClaro.triggered.connect(self.cambiar_claro)
        self.ui.actionOscuro.triggered.connect(self.cambiar_oscuro)
        self.ui.actionOscuro.setChecked(True)
        self.cambiar_oscuro()

    @Slot()
    def load_projects(self):
        self.ui.projects.clear()
        for root, subdirs, files in os.walk(self.ruta_buscar):
            for d in subdirs:
                if os.access(root, os.R_OK):
                    if d == ".git":
                        folder_name = root.split(os.sep)[-1]
                        item = QListWidgetItem()
                        item.setText(folder_name)
                        item.setToolTip(root)
                        self.ui.projects.addItem(item)
                else:
                    print(d + " No permission")
        self.ui.projects.clicked.connect(self.item_clicked)
        self.ui.loadingGif.setHidden(True)
        self.ui.btnUpdate.setEnabled(True)

    @Slot()
    def thread_load_projects(self):
        self.ui.loadingGif.setHidden(False)
        self.ui.btnUpdate.setDisabled(True)
        self.thread_manager.start(self.load_projects)

    def item_clicked(self):
        item = self.ui.projects.currentItem()
        self.project(item.toolTip())

    def get_route(self):
        nueva_ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", self.home)
        if nueva_ruta:
            self.ruta_buscar = nueva_ruta
            self.ui.rutaEdit.setText(nueva_ruta)
            self.thread_load_projects()

    def set_route(self, text):
        self.ruta_buscar = text

    def clone(self):
        self.clonar = Clone(self.ui.actionOscuro.isChecked())
        self.clonar.show()

    def project(self, project):
        self.proyecto = Project(project, self.ui.actionOscuro.isChecked())
        self.proyecto.show()

    def cambiar_claro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.clonar.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.proyecto.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.ui.btnInfo.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/info.png")))
        self.ui.labelTusProyectos.setStyleSheet("""QLabel
                                                       {
                                                       font: 700 18pt "Segoe UI";
                                                       }
                                                       """)

    def cambiar_oscuro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet())
        self.clonar.setStyleSheet(qdarktheme.load_stylesheet())
        self.proyecto.setStyleSheet(qdarktheme.load_stylesheet())
        self.ui.btnInfo.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/info_w.png")))
        self.ui.labelTusProyectos.setStyleSheet("""QLabel
                                                       {
                                                       font: 700 18pt "Segoe UI";
                                                       }
                                                       """)


if __name__ == "__main__":
    app = QApplication([])
    widget = GitManager()
    widget.show()
    sys.exit(app.exec())
