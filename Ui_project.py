# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_project(object):
    def setupUi(self, project):
        if not project.objectName():
            project.setObjectName(u"project")
        project.resize(800, 750)
        self.actionConfiguraci_n = QAction(project)
        self.actionConfiguraci_n.setObjectName(u"actionConfiguraci_n")
        self.actionAcerca_de = QAction(project)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.verticalLayout_2 = QVBoxLayout(project)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.repoNameLabel = QLabel(project)
        self.repoNameLabel.setObjectName(u"repoNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repoNameLabel.sizePolicy().hasHeightForWidth())
        self.repoNameLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.repoNameLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.repoNameLabel)

        self.infoLabel = QLabel(project)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_2.addWidget(self.infoLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.nombreCompletoLabel = QLabel(project)
        self.nombreCompletoLabel.setObjectName(u"nombreCompletoLabel")
        self.nombreCompletoLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nombreCompletoLabel)

        self.nombreCompletoLineEdit = QLineEdit(project)
        self.nombreCompletoLineEdit.setObjectName(u"nombreCompletoLineEdit")
        self.nombreCompletoLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nombreCompletoLineEdit)

        self.descrLabel = QLabel(project)
        self.descrLabel.setObjectName(u"descrLabel")
        self.descrLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.descrLabel)

        self.descLineEdit = QLineEdit(project)
        self.descLineEdit.setObjectName(u"descLineEdit")
        self.descLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.descLineEdit)

        self.fechaCreaLabel = QLabel(project)
        self.fechaCreaLabel.setObjectName(u"fechaCreaLabel")
        self.fechaCreaLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.fechaCreaLabel)

        self.fechaCreaLineEdit = QLineEdit(project)
        self.fechaCreaLineEdit.setObjectName(u"fechaCreaLineEdit")
        self.fechaCreaLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.fechaCreaLineEdit)

        self.ultimaActualizacionLabel = QLabel(project)
        self.ultimaActualizacionLabel.setObjectName(u"ultimaActualizacionLabel")
        self.ultimaActualizacionLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.ultimaActualizacionLabel)

        self.ultimaActualizacionLineEdit = QLineEdit(project)
        self.ultimaActualizacionLineEdit.setObjectName(u"ultimaActualizacionLineEdit")
        self.ultimaActualizacionLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.ultimaActualizacionLineEdit)

        self.pgIniLabel = QLabel(project)
        self.pgIniLabel.setObjectName(u"pgIniLabel")
        self.pgIniLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.pgIniLabel)

        self.pgIniLineEdit = QLineEdit(project)
        self.pgIniLineEdit.setObjectName(u"pgIniLineEdit")
        self.pgIniLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.pgIniLineEdit)

        self.lenguajeLabel = QLabel(project)
        self.lenguajeLabel.setObjectName(u"lenguajeLabel")
        self.lenguajeLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lenguajeLabel)

        self.lenguajeLineEdit = QLineEdit(project)
        self.lenguajeLineEdit.setObjectName(u"lenguajeLineEdit")
        self.lenguajeLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lenguajeLineEdit)

        self.forksLabel = QLabel(project)
        self.forksLabel.setObjectName(u"forksLabel")
        self.forksLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.forksLabel)

        self.forksLineEdit = QLineEdit(project)
        self.forksLineEdit.setObjectName(u"forksLineEdit")
        self.forksLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.forksLineEdit)

        self.estrellasLabel = QLabel(project)
        self.estrellasLabel.setObjectName(u"estrellasLabel")
        self.estrellasLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.estrellasLabel)

        self.estrellasLineEdit = QLineEdit(project)
        self.estrellasLineEdit.setObjectName(u"estrellasLineEdit")
        self.estrellasLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.estrellasLineEdit)

        self.licenciaLabel = QLabel(project)
        self.licenciaLabel.setObjectName(u"licenciaLabel")
        self.licenciaLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.licenciaLabel)

        self.licenciaLineEdit = QLineEdit(project)
        self.licenciaLineEdit.setObjectName(u"licenciaLineEdit")
        self.licenciaLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.licenciaLineEdit)

        self.commitsLabel = QLabel(project)
        self.commitsLabel.setObjectName(u"commitsLabel")
        self.commitsLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.commitsLabel)

        self.commitsWidget = QWidget(project)
        self.commitsWidget.setObjectName(u"commitsWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.commitsWidget.sizePolicy().hasHeightForWidth())
        self.commitsWidget.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.commitsWidget)

        self.creadorLabel = QLabel(project)
        self.creadorLabel.setObjectName(u"creadorLabel")
        self.creadorLabel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.creadorLabel)

        self.creadorLineEdit = QLineEdit(project)
        self.creadorLineEdit.setObjectName(u"creadorLineEdit")
        self.creadorLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.creadorLineEdit)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.actualizarInformacionBtn = QPushButton(project)
        self.actualizarInformacionBtn.setObjectName(u"actualizarInformacionBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.actualizarInformacionBtn.sizePolicy().hasHeightForWidth())
        self.actualizarInformacionBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.actualizarInformacionBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.abrirCarpetaBtn = QPushButton(project)
        self.abrirCarpetaBtn.setObjectName(u"abrirCarpetaBtn")
        sizePolicy2.setHeightForWidth(self.abrirCarpetaBtn.sizePolicy().hasHeightForWidth())
        self.abrirCarpetaBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.abrirCarpetaBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(project)

        QMetaObject.connectSlotsByName(project)
    # setupUi

    def retranslateUi(self, project):
        project.setWindowTitle(QCoreApplication.translate("project", u"github", None))
        self.actionConfiguraci_n.setText(QCoreApplication.translate("project", u"Configuraci\u00f3n", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("project", u"Acerca de", None))
        self.repoNameLabel.setText(QCoreApplication.translate("project", u"repo", None))
        self.infoLabel.setText("")
        self.nombreCompletoLabel.setText(QCoreApplication.translate("project", u"Nombre completo", None))
        self.descrLabel.setText(QCoreApplication.translate("project", u"Descripci\u00f3n", None))
        self.fechaCreaLabel.setText(QCoreApplication.translate("project", u"Fecha creaci\u00f3n", None))
        self.ultimaActualizacionLabel.setText(QCoreApplication.translate("project", u"\u00daltima actualizaci\u00f3n", None))
        self.pgIniLabel.setText(QCoreApplication.translate("project", u"P\u00e1gina de inicio", None))
        self.lenguajeLabel.setText(QCoreApplication.translate("project", u"Lenguaje", None))
        self.forksLabel.setText(QCoreApplication.translate("project", u"Forks", None))
        self.estrellasLabel.setText(QCoreApplication.translate("project", u"Estrellas", None))
        self.licenciaLabel.setText(QCoreApplication.translate("project", u"Licencia", None))
        self.commitsLabel.setText(QCoreApplication.translate("project", u"Commits", None))
        self.creadorLabel.setText(QCoreApplication.translate("project", u"Creador", None))
        self.actualizarInformacionBtn.setText(QCoreApplication.translate("project", u"Actualizar informaci\u00f3n", None))
        self.abrirCarpetaBtn.setText(QCoreApplication.translate("project", u"Abrir carpeta", None))
    # retranslateUi

