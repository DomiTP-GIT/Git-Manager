# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_gitManager(object):
    def setupUi(self, gitManager):
        if not gitManager.objectName():
            gitManager.setObjectName(u"gitManager")
        gitManager.resize(800, 600)
        self.actionConfig = QAction(gitManager)
        self.actionConfig.setObjectName(u"actionConfig")
        self.actionAcerca_de = QAction(gitManager)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.actionClaro = QAction(gitManager)
        self.actionClaro.setObjectName(u"actionClaro")
        self.actionClaro.setCheckable(True)
        self.actionOscuro = QAction(gitManager)
        self.actionOscuro.setObjectName(u"actionOscuro")
        self.actionOscuro.setCheckable(True)
        self.centralwidget = QWidget(gitManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.btnClonar = QPushButton(self.centralwidget)
        self.btnClonar.setObjectName(u"btnClonar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClonar.sizePolicy().hasHeightForWidth())
        self.btnClonar.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnClonar)

        self.btnUpdate = QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName(u"btnUpdate")
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnUpdate)

        self.loadingGif = QLabel(self.centralwidget)
        self.loadingGif.setObjectName(u"loadingGif")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loadingGif.sizePolicy().hasHeightForWidth())
        self.loadingGif.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.loadingGif)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.rutaEdit = QLineEdit(self.centralwidget)
        self.rutaEdit.setObjectName(u"rutaEdit")
        self.rutaEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.rutaEdit)

        self.btnRuta = QPushButton(self.centralwidget)
        self.btnRuta.setObjectName(u"btnRuta")
        sizePolicy.setHeightForWidth(self.btnRuta.sizePolicy().hasHeightForWidth())
        self.btnRuta.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnRuta)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.projects = QListWidget(self.centralwidget)
        self.projects.setObjectName(u"projects")

        self.gridLayout.addWidget(self.projects, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.btnInfo = QPushButton(self.centralwidget)
        self.btnInfo.setObjectName(u"btnInfo")
        sizePolicy.setHeightForWidth(self.btnInfo.sizePolicy().hasHeightForWidth())
        self.btnInfo.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"resources/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInfo.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btnInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        gitManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(gitManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuModo = QMenu(self.menuArchivo)
        self.menuModo.setObjectName(u"menuModo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        gitManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(gitManager)
        self.statusbar.setObjectName(u"statusbar")
        gitManager.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.menuModo.menuAction())
        self.menuModo.addAction(self.actionClaro)
        self.menuModo.addAction(self.actionOscuro)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(gitManager)

        QMetaObject.connectSlotsByName(gitManager)
    # setupUi

    def retranslateUi(self, gitManager):
        gitManager.setWindowTitle(QCoreApplication.translate("gitManager", u"github", None))
        self.actionConfig.setText(QCoreApplication.translate("gitManager", u"Configuraci\u00f3n", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("gitManager", u"Acerca de", None))
        self.actionClaro.setText(QCoreApplication.translate("gitManager", u"Claro", None))
#if QT_CONFIG(tooltip)
        self.actionClaro.setToolTip(QCoreApplication.translate("gitManager", u"Activa el modo claro de la aplicaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.actionOscuro.setText(QCoreApplication.translate("gitManager", u"Oscuro", None))
#if QT_CONFIG(tooltip)
        self.actionOscuro.setToolTip(QCoreApplication.translate("gitManager", u"Activa el modo oscuro en la aplicaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Muestra los proyectos que se encuentran detro de la ruta de b\u00fasqueda</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("gitManager", u"Tus proyectos", None))
#if QT_CONFIG(tooltip)
        self.btnClonar.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Descarga/clona nuevos repositorios a t\u00fa ordenador</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnClonar.setText(QCoreApplication.translate("gitManager", u"Clonar repositorios", None))
#if QT_CONFIG(tooltip)
        self.btnUpdate.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Actualiza la lista de proyectos</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnUpdate.setText(QCoreApplication.translate("gitManager", u"Actualizar", None))
        self.loadingGif.setText("")
#if QT_CONFIG(tooltip)
        self.rutaEdit.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Ruta de b\u00fasqueda de repositorios</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnRuta.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Seleccionar una nueva ruta para buscar dispositivos</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnRuta.setText(QCoreApplication.translate("gitManager", u"Seleccionar ruta", None))
        self.label_2.setText(QCoreApplication.translate("gitManager", u"Ruta de b\u00fasqueda:", None))
#if QT_CONFIG(tooltip)
        self.btnInfo.setToolTip(QCoreApplication.translate("gitManager", u"<html><head/><body><p>Se buscar\u00e1n todos los repositorios git que se encuentren en cualquier subruta de esta ruta.</p><p>La ruta por defecto es el home del usuario que ejecuta el programa.</p><p>No podremos obtener informaci\u00f3n de los proyectos si no tiene los permisos necesarios en dichas carpetas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnInfo.setText("")
        self.menuArchivo.setTitle(QCoreApplication.translate("gitManager", u"Archivo", None))
        self.menuModo.setTitle(QCoreApplication.translate("gitManager", u"Modo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("gitManager", u"Ayuda", None))
    # retranslateUi

