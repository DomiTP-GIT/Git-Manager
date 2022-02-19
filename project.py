# This Python file uses the following encoding: utf-8
import base64

import qdarktheme
from PySide6.QtWidgets import QWidget
from git import Repo
from github import Github

from Ui_project import Ui_project


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

        self.g = Github('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')
        self.get_repo_info()

        self.config()
        self.load_ui()

    def config(self):
        if self.darkTheme:
            self.cambiar_oscuro()
        else:
            self.cambiar_claro()

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
