# This Python file uses the following encoding: utf-8
import os
import re
from pathlib import Path

import git
import qdarktheme
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox

from Ui_clone import Ui_clone


class Clone(QWidget):
    def __init__(self, dark_theme):
        super(Clone, self).__init__()
        self.darkTheme = dark_theme
        self.ui = Ui_clone()
        self.ui.setupUi(self)

        self.home = str(Path.home())

        self.config()

    def config(self):
        if self.darkTheme:
            self.cambiar_oscuro()
        else:
            self.cambiar_claro()

        self.ui.btnClonar.setEnabled(False)
        self.ui.editRutaGuardado.textChanged.connect(self.activar_clonar)
        self.ui.editRutaArchivo.textChanged.connect(self.activar_clonar)
        self.ui.urlText.textChanged.connect(self.activar_clonar)
        self.ui.btnClonar.clicked.connect(self.clonar)
        self.ui.btnSeleccionarDirectorios.clicked.connect(self.ruta_guardado)
        self.ui.btnSeleccionarArchivos.clicked.connect(self.ruta_archivo)

    def cambiar_claro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet("light"))

    def cambiar_oscuro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet())

    def activar_clonar(self):
        self.ui.labelRutaGuardadoError.setText("")
        self.ui.labelRutaArchivoError.setText("")
        if (len(self.ui.urlText.toPlainText()) > 0 or len(self.ui.editRutaArchivo.text()) > 0) and len(
                self.ui.editRutaGuardado.text()) > 0:
            self.ui.btnClonar.setEnabled(True)
        else:
            self.ui.btnClonar.setEnabled(False)

    def ruta_guardado(self):
        nueva_ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", self.home)
        if nueva_ruta:
            self.ui.editRutaGuardado.setText(nueva_ruta)

    def ruta_archivo(self):
        nueva_ruta = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Text Files (*.txt)")
        if nueva_ruta:
            self.ui.editRutaArchivo.setText(nueva_ruta[0])

    def comprobar_url(self, url):
        valid = False
        if re.search("((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?", url):
            valid = True
        elif re.search("((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?", url + ".git"):
            valid = True
        return valid

    def comprobar_ruta_guardado(self):
        directorio = self.ui.editRutaGuardado.text()
        ok = False
        if os.path.exists(directorio):
            if os.path.isdir(directorio):
                if os.access(directorio, os.R_OK | os.W_OK):
                    ok = True
                else:
                    self.ui.labelRutaGuardadoError.setText("No tienes permisos en el directorio")
            else:
                self.ui.labelRutaGuardadoError.setText("La ruta especificada no es un directorio")
        else:
            self.ui.labelRutaGuardadoError.setText("La ruta especificada no existe")
        return ok

    def comprobar_archivo_repositorios(self, archivo):
        ok = False
        if os.path.exists(archivo):
            if os.path.isfile(archivo):
                if os.access(archivo, os.R_OK):
                    ok = True
                else:
                    self.ui.labelRutaArchivoError.setText("No tienes permisos en el directorio")
            else:
                self.ui.labelRutaArchivoError.setText("La ruta especificada no es un directorio")
        else:
            self.ui.labelRutaArchivoError.setText("La ruta especificada no existe")
        return ok

    def confirm_dialog(self, bad_repos):
        confirm = QMessageBox()
        confirm.setIcon(QMessageBox.Warning)
        confirm.setWindowTitle("Clonar")
        confirm.setText("Tienes enlaces a repositorios no válidos")
        confirm.setInformativeText("¿Quieres clonar los válidos?")
        txt = "Repositorios erróneos:" + "\n".join(bad_repos)
        confirm.setDetailedText(txt)
        confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        res = confirm.exec()
        if res == QMessageBox.Yes:
            return True
        else:
            return False

    def clonar(self):
        if self.comprobar_ruta_guardado():
            repos = []
            bad_repos = []
            if len(self.ui.urlText.toPlainText()) > 0:
                tmp = self.ui.urlText.toPlainText().split('\n')
                for repo in tmp:
                    if self.comprobar_url(repo):
                        repos.append(repo)
                    else:
                        bad_repos.append(repo)
            if len(self.ui.editRutaArchivo.text()) > 0 and self.comprobar_archivo_repositorios(
                    self.ui.editRutaArchivo.text()):
                with open(self.ui.editRutaArchivo.text()) as f:
                    contenido = f.read()
                    contenido = contenido.split('\n')
                    for repo in contenido:
                        if self.comprobar_url(repo):
                            repos.append(repo)
                        else:
                            bad_repos.append(repo)

            if len(repos) > 0:  # Si hay repositorios para clonar
                guardado = self.ui.editRutaGuardado.text()
                continuar = True
                if len(bad_repos) > 0:  # Si la lista de repositorios incorrectos tiene algo muestra un diálogo
                    if not self.confirm_dialog(bad_repos):
                        continuar = False  # El usuario no quiere continuar clonando los repositorios
                if continuar:
                    for repo in repos:
                        repo_name = repo.split('.git')[0].split('/')[-1]
                        ruta = os.path.join(guardado, repo_name)
                        if not os.path.exists(ruta) and not os.path.isdir(ruta):
                            try:
                                git.Repo.clone_from(repo, os.path.join(guardado, repo_name))
                            except:
                                print("Error al clonar un repositorio")
                            dlg = QMessageBox(self)
                            dlg.information(self, "Clonado", "El clonado de los repositorios ha finalizado.",
                                            QMessageBox.Ok)
