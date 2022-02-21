# This Python file uses the following encoding: utf-8
import base64
import os.path
from datetime import datetime

import qdarktheme
import requests
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget
from git import Repo
from github import Github
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from Ui_project import Ui_project
from config_files import Config


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=6, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)
        self.ax.set(xlabel='commits totales', ylabel='semanas', title='Commits por semanas')


class Project(QWidget):
    def __init__(self, project, dark_theme):
        super(Project, self).__init__()
        self.project = project
        self.darkTheme = dark_theme

        self.ui = Ui_project()
        self.ui.setupUi(self)

        self.username = ""
        self.projectName = ""
        self.fullRepoName = ""

        self.config = Config()

        if self.config.is_token_saved():
            self.g = Github(self.config.get_token())
        else:
            self.g = Github()

        self.get_repo_info()

        self.load_config()
        self.load_ui()

    def load_config(self):
        if self.darkTheme:
            self.cambiar_oscuro()
        else:
            self.cambiar_claro()
        self.ui.actualizarInformacionBtn.clicked.connect(self.refresh_info)
        self.ui.abrirCarpetaBtn.clicked.connect(self.open_in_explorer)

    def load_ui(self):
        self.ui.repoNameLabel.setText(self.projectName.upper())
        try:
            repo = self.g.get_repo(self.fullRepoName)
            self.ui.nombreCompletoLineEdit.setText(repo.full_name)
            self.ui.creadorLineEdit.setText(repo.owner.name)
            self.ui.descLineEdit.setText(repo.description)
            self.ui.fechaCreaLineEdit.setText(str(repo.created_at))
            self.ui.ultimaActualizacionLineEdit.setText(str(repo.pushed_at))
            self.ui.pgIniLineEdit.setText(repo.homepage)
            self.ui.lenguajeLineEdit.setText(repo.language)
            self.ui.forksLineEdit.setText(str(repo.forks))
            self.ui.estrellasLineEdit.setText(str(repo.stargazers_count))
            try:
                self.ui.licenciaLineEdit.setText(base64.b64decode(repo.get_license().content.encode()).decode())
            except:
                self.ui.licenciaLineEdit.setText('')
            self.plot()
        except:
            self.ui.infoLabel.setText("El repositorio es privado o no está alojado en GitHub")
            self.ui.nombreCompletoLineEdit.setText(self.fullRepoName)
            self.ui.creadorLineEdit.setText(self.username)

    def get_repo_info(self):
        repo = Repo(self.project)
        repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
        repo_user = repo.remotes.origin.url.split('.git')[0].split('/')[-2]
        if ":" in repo_user:
            repo_user = repo_user.split(':')[-1]
        full_repo_name = f'{repo_user}/{repo_name}'

        self.username = repo_user
        self.projectName = repo_name
        self.fullRepoName = full_repo_name

        return full_repo_name

    def cambiar_claro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet("light"))

    def cambiar_oscuro(self):
        self.setStyleSheet(qdarktheme.load_stylesheet())

    def refresh_info(self):
        self.get_repo_info()
        self.load_ui()

    def open_in_explorer(self):
        fullpath = os.path.realpath(self.project)
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(fullpath)):
            print("Error al abrir archivo en explorador")

    def plot(self):
        response = requests.get(f'https://api.github.com/repos/{self.fullRepoName}/stats/commit_activity')
        weeks = []
        total = []
        if response.status_code == 200:
            for x in response.json():
                weeks.append(datetime.fromtimestamp(x["week"]).strftime('%m/%d'))
                total.append(x["total"])
            weeks = weeks[36:]
            total = total[36:]
            self.ui.commitsWidget = MplCanvas(self.ui.commitsWidget, width=10, height=6, dpi=50)
            self.ui.commitsWidget.ax.bar(weeks, total)
