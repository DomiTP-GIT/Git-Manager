# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clone.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_clone(object):
    def setupUi(self, clone):
        if not clone.objectName():
            clone.setObjectName(u"clone")
        clone.resize(800, 600)
        self.actionConfiguraci_n = QAction(clone)
        self.actionConfiguraci_n.setObjectName(u"actionConfiguraci_n")
        self.actionAcerca_de = QAction(clone)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.verticalLayout_3 = QVBoxLayout(clone)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(clone)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label)

        self.urlText = QPlainTextEdit(clone)
        self.urlText.setObjectName(u"urlText")
        self.urlText.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_2.addWidget(self.urlText)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(clone)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.labelRutaArchivoError = QLabel(clone)
        self.labelRutaArchivoError.setObjectName(u"labelRutaArchivoError")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelRutaArchivoError.sizePolicy().hasHeightForWidth())
        self.labelRutaArchivoError.setSizePolicy(sizePolicy1)
        self.labelRutaArchivoError.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_5.addWidget(self.labelRutaArchivoError)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.editRutaArchivo = QLineEdit(clone)
        self.editRutaArchivo.setObjectName(u"editRutaArchivo")

        self.horizontalLayout_3.addWidget(self.editRutaArchivo)

        self.btnSeleccionarArchivos = QPushButton(clone)
        self.btnSeleccionarArchivos.setObjectName(u"btnSeleccionarArchivos")

        self.horizontalLayout_3.addWidget(self.btnSeleccionarArchivos)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(clone)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.labelRutaGuardadoError = QLabel(clone)
        self.labelRutaGuardadoError.setObjectName(u"labelRutaGuardadoError")
        self.labelRutaGuardadoError.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.labelRutaGuardadoError)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.editRutaGuardado = QLineEdit(clone)
        self.editRutaGuardado.setObjectName(u"editRutaGuardado")
        sizePolicy2.setHeightForWidth(self.editRutaGuardado.sizePolicy().hasHeightForWidth())
        self.editRutaGuardado.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.editRutaGuardado)

        self.btnSeleccionarDirectorios = QPushButton(clone)
        self.btnSeleccionarDirectorios.setObjectName(u"btnSeleccionarDirectorios")

        self.horizontalLayout_2.addWidget(self.btnSeleccionarDirectorios)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btnClonar = QPushButton(clone)
        self.btnClonar.setObjectName(u"btnClonar")

        self.verticalLayout_2.addWidget(self.btnClonar)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(clone)

        QMetaObject.connectSlotsByName(clone)
    # setupUi

    def retranslateUi(self, clone):
        clone.setWindowTitle(QCoreApplication.translate("clone", u"github", None))
        self.actionConfiguraci_n.setText(QCoreApplication.translate("clone", u"Configuraci\u00f3n", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("clone", u"Acerca de", None))
        self.label.setText(QCoreApplication.translate("clone", u"Introduce las URL a descargar:", None))
        self.urlText.setPlaceholderText(QCoreApplication.translate("clone", u"https://github.com/DomiTP-GIT/Git-Manager.git", None))
        self.label_3.setText(QCoreApplication.translate("clone", u"Selecciona el archivo que contenga los repositorios:", None))
        self.labelRutaArchivoError.setText("")
        self.btnSeleccionarArchivos.setText(QCoreApplication.translate("clone", u"Seleccionar archivo", None))
        self.label_2.setText(QCoreApplication.translate("clone", u"Ruta de guardado:", None))
        self.labelRutaGuardadoError.setText("")
        self.btnSeleccionarDirectorios.setText(QCoreApplication.translate("clone", u"Seleccionar directorio", None))
        self.btnClonar.setText(QCoreApplication.translate("clone", u"Clonar", None))
    # retranslateUi

