# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 656)
        self.actionCalculate = QAction(MainWindow)
        self.actionCalculate.setObjectName(u"actionCalculate")
        self.actionGet_Graph = QAction(MainWindow)
        self.actionGet_Graph.setObjectName(u"actionGet_Graph")
        self.actionClear_History = QAction(MainWindow)
        self.actionClear_History.setObjectName(u"actionClear_History")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 418, 267))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_equacao = QLineEdit(self.frame_2)
        self.line_equacao.setObjectName(u"line_equacao")
        self.line_equacao.setFrame(False)

        self.verticalLayout_2.addWidget(self.line_equacao)

        self.line_avisos = QLineEdit(self.frame_2)
        self.line_avisos.setObjectName(u"line_avisos")
        self.line_avisos.setFrame(False)
        self.line_avisos.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.line_avisos)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.botao_divide = QPushButton(self.frame)
        self.botao_divide.setObjectName(u"botao_divide")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_divide.sizePolicy().hasHeightForWidth())
        self.botao_divide.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_divide, 1, 3, 1, 1)

        self.botao_7 = QPushButton(self.frame)
        self.botao_7.setObjectName(u"botao_7")
        sizePolicy.setHeightForWidth(self.botao_7.sizePolicy().hasHeightForWidth())
        self.botao_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_7, 1, 0, 1, 1)

        self.botao_6 = QPushButton(self.frame)
        self.botao_6.setObjectName(u"botao_6")
        sizePolicy.setHeightForWidth(self.botao_6.sizePolicy().hasHeightForWidth())
        self.botao_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_6, 2, 2, 1, 1)

        self.botao_fecha_parenteses = QPushButton(self.frame)
        self.botao_fecha_parenteses.setObjectName(u"botao_fecha_parenteses")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botao_fecha_parenteses.sizePolicy().hasHeightForWidth())
        self.botao_fecha_parenteses.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.botao_fecha_parenteses, 0, 2, 1, 1)

        self.botao_8 = QPushButton(self.frame)
        self.botao_8.setObjectName(u"botao_8")
        sizePolicy.setHeightForWidth(self.botao_8.sizePolicy().hasHeightForWidth())
        self.botao_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_8, 1, 1, 1, 1)

        self.botao_pi = QPushButton(self.frame)
        self.botao_pi.setObjectName(u"botao_pi")
        sizePolicy1.setHeightForWidth(self.botao_pi.sizePolicy().hasHeightForWidth())
        self.botao_pi.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.botao_pi, 0, 4, 1, 1)

        self.botao_5 = QPushButton(self.frame)
        self.botao_5.setObjectName(u"botao_5")
        sizePolicy.setHeightForWidth(self.botao_5.sizePolicy().hasHeightForWidth())
        self.botao_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_5, 2, 1, 1, 1)

        self.botao_modulo = QPushButton(self.frame)
        self.botao_modulo.setObjectName(u"botao_modulo")
        sizePolicy1.setHeightForWidth(self.botao_modulo.sizePolicy().hasHeightForWidth())
        self.botao_modulo.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.botao_modulo, 0, 3, 1, 1)

        self.botao_adicao = QPushButton(self.frame)
        self.botao_adicao.setObjectName(u"botao_adicao")
        sizePolicy.setHeightForWidth(self.botao_adicao.sizePolicy().hasHeightForWidth())
        self.botao_adicao.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_adicao, 3, 3, 1, 1)

        self.botao_ponto = QPushButton(self.frame)
        self.botao_ponto.setObjectName(u"botao_ponto")
        sizePolicy.setHeightForWidth(self.botao_ponto.sizePolicy().hasHeightForWidth())
        self.botao_ponto.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_ponto, 4, 0, 1, 1)

        self.botao_zero = QPushButton(self.frame)
        self.botao_zero.setObjectName(u"botao_zero")
        sizePolicy.setHeightForWidth(self.botao_zero.sizePolicy().hasHeightForWidth())
        self.botao_zero.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_zero, 4, 1, 1, 1)

        self.botao_3 = QPushButton(self.frame)
        self.botao_3.setObjectName(u"botao_3")
        sizePolicy.setHeightForWidth(self.botao_3.sizePolicy().hasHeightForWidth())
        self.botao_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_3, 3, 2, 1, 1)

        self.botao_calcular = QPushButton(self.frame)
        self.botao_calcular.setObjectName(u"botao_calcular")
        sizePolicy.setHeightForWidth(self.botao_calcular.sizePolicy().hasHeightForWidth())
        self.botao_calcular.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_calcular, 3, 4, 2, 1)

        self.botao_percent = QPushButton(self.frame)
        self.botao_percent.setObjectName(u"botao_percent")
        sizePolicy.setHeightForWidth(self.botao_percent.sizePolicy().hasHeightForWidth())
        self.botao_percent.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_percent, 4, 2, 1, 1)

        self.botao_1 = QPushButton(self.frame)
        self.botao_1.setObjectName(u"botao_1")
        sizePolicy.setHeightForWidth(self.botao_1.sizePolicy().hasHeightForWidth())
        self.botao_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_1, 3, 0, 1, 1)

        self.botao_raiz_quadrada = QPushButton(self.frame)
        self.botao_raiz_quadrada.setObjectName(u"botao_raiz_quadrada")
        sizePolicy.setHeightForWidth(self.botao_raiz_quadrada.sizePolicy().hasHeightForWidth())
        self.botao_raiz_quadrada.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_raiz_quadrada, 1, 4, 1, 1)

        self.botao_2 = QPushButton(self.frame)
        self.botao_2.setObjectName(u"botao_2")
        sizePolicy.setHeightForWidth(self.botao_2.sizePolicy().hasHeightForWidth())
        self.botao_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_2, 3, 1, 1, 1)

        self.botao_multiplica = QPushButton(self.frame)
        self.botao_multiplica.setObjectName(u"botao_multiplica")
        sizePolicy.setHeightForWidth(self.botao_multiplica.sizePolicy().hasHeightForWidth())
        self.botao_multiplica.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_multiplica, 2, 3, 1, 1)

        self.botao_subtracao = QPushButton(self.frame)
        self.botao_subtracao.setObjectName(u"botao_subtracao")
        sizePolicy.setHeightForWidth(self.botao_subtracao.sizePolicy().hasHeightForWidth())
        self.botao_subtracao.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_subtracao, 4, 3, 1, 1)

        self.botao_4 = QPushButton(self.frame)
        self.botao_4.setObjectName(u"botao_4")
        sizePolicy.setHeightForWidth(self.botao_4.sizePolicy().hasHeightForWidth())
        self.botao_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_4, 2, 0, 1, 1)

        self.botao_backspace = QPushButton(self.frame)
        self.botao_backspace.setObjectName(u"botao_backspace")
        sizePolicy1.setHeightForWidth(self.botao_backspace.sizePolicy().hasHeightForWidth())
        self.botao_backspace.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.botao_backspace, 0, 0, 1, 1)

        self.botao_abre_parenteses = QPushButton(self.frame)
        self.botao_abre_parenteses.setObjectName(u"botao_abre_parenteses")
        sizePolicy1.setHeightForWidth(self.botao_abre_parenteses.sizePolicy().hasHeightForWidth())
        self.botao_abre_parenteses.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.botao_abre_parenteses, 0, 1, 1, 1)

        self.botao_9 = QPushButton(self.frame)
        self.botao_9.setObjectName(u"botao_9")
        sizePolicy.setHeightForWidth(self.botao_9.sizePolicy().hasHeightForWidth())
        self.botao_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_9, 1, 2, 1, 1)

        self.botao_quadrado = QPushButton(self.frame)
        self.botao_quadrado.setObjectName(u"botao_quadrado")
        sizePolicy.setHeightForWidth(self.botao_quadrado.sizePolicy().hasHeightForWidth())
        self.botao_quadrado.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.botao_quadrado, 2, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 26))
        self.menu_clear_equation = QMenu(self.menubar)
        self.menu_clear_equation.setObjectName(u"menu_clear_equation")
        self.menu_clear_history = QMenu(self.menubar)
        self.menu_clear_history.setObjectName(u"menu_clear_history")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_clear_equation.menuAction())
        self.menubar.addAction(self.menu_clear_history.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.actionGet_Graph.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.actionClear_History.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Fira Sans Semi-Light'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.botao_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.botao_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.botao_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.botao_fecha_parenteses.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.botao_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.botao_pi.setText(QCoreApplication.translate("MainWindow", u"pi", None))
        self.botao_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.botao_modulo.setText(QCoreApplication.translate("MainWindow", u"mod", None))
        self.botao_adicao.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.botao_ponto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.botao_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.botao_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.botao_calcular.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.botao_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.botao_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.botao_raiz_quadrada.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.botao_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.botao_multiplica.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.botao_subtracao.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.botao_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.botao_backspace.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.botao_abre_parenteses.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.botao_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.botao_quadrado.setText(QCoreApplication.translate("MainWindow", u"^2", None))
        self.menu_clear_equation.setTitle(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menu_clear_history.setTitle(QCoreApplication.translate("MainWindow", u"Clear History", None))
    # retranslateUi

