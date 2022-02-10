# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QListWidgetItem, QFileDialog


class GithubManager(QMainWindow):
    def __init__(self):
        super(GithubManager, self).__init__()
        self.window = self.load_ui()
        self.window.setWindowTitle("Git Manager")
        self.window.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/githubmanager.png")))

        self.home = str(Path.home())
        self.ruta_buscar = self.home

        self.config()
        self.load_projects()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "main.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        return loader.load(path, self)
        # ui_file.close()

    def config(self):
        self.window.projects.setStyleSheet("QListWidget"
                                           "{"
                                           "background-color : rgb(206, 206, 206)"
                                           "}"
                                           "QListView::item"
                                           "{"
                                           "padding : 10px;"
                                           "border-bottom : 0.5px solid rgb(184, 184, 184);"
                                           "background-color : rgb(255, 255, 255)"
                                           "}"
                                           "QListView::item:selected"
                                           "{"
                                           "background-color : rgb(59, 168, 255);"
                                           "color : black"
                                           "}"
                                           "QListView::item:hover"
                                           "{"
                                           "background-color : rgb(59, 168, 255);"
                                           "}"
                                           )
        self.window.projects.setAlternatingRowColors(True)
        self.window.projects.setDragDropMode(QAbstractItemView.InternalMove)
        self.window.btnRuta.clicked.connect(self.get_route)
        self.window.rutaEdit.setText(self.ruta_buscar)
        self.window.btn_update.clicked.connect(self.load_projects)

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


if __name__ == "__main__":
    app = QApplication([])
    widget = GithubManager()
    widget.window.show()
    sys.exit(app.exec())
