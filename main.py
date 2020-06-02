# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from fonc import convertCRScoords_Unic, convertCRScoords_Quato, convertGeoCRScoords

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 587)
        MainWindow.setStyleSheet("background-color rgb(184, 184, 184)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 311, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 140, 301, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 50, 291, 16))
        self.label_5.setObjectName("label_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(340, 70, 141, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 70, 191, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 90, 191, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 110, 191, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 130, 191, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 30, 291, 16))
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(720, 70, 121, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(720, 90, 121, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(720, 110, 121, 21))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(720, 130, 121, 21))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(490, 220, 191, 16))
        self.label_11.setObjectName("label_11")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(720, 200, 121, 21))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 200, 191, 16))
        self.label_12.setObjectName("label_12")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(720, 260, 121, 21))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(490, 260, 191, 16))
        self.label_13.setObjectName("label_13")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(720, 240, 121, 21))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(490, 240, 191, 16))
        self.label_14.setObjectName("label_14")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(720, 220, 121, 21))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(340, 200, 141, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(490, 280, 191, 16))
        self.label_15.setObjectName("label_15")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(720, 280, 121, 21))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(490, 300, 191, 16))
        self.label_16.setObjectName("label_16")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(720, 300, 121, 21))
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(720, 430, 121, 21))
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(490, 390, 191, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(490, 410, 191, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(490, 370, 191, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(490, 450, 191, 16))
        self.label_20.setObjectName("label_20")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(720, 350, 121, 21))
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.plainTextEdit_14 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_14.setGeometry(QtCore.QRect(720, 410, 121, 21))
        self.plainTextEdit_14.setObjectName("plainTextEdit_14")
        self.plainTextEdit_15 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_15.setGeometry(QtCore.QRect(720, 370, 121, 21))
        self.plainTextEdit_15.setObjectName("plainTextEdit_15")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(490, 350, 191, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(490, 430, 191, 16))
        self.label_22.setObjectName("label_22")
        self.plainTextEdit_16 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_16.setGeometry(QtCore.QRect(720, 390, 121, 21))
        self.plainTextEdit_16.setObjectName("plainTextEdit_16")
        self.plainTextEdit_17 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_17.setGeometry(QtCore.QRect(720, 450, 121, 21))
        self.plainTextEdit_17.setObjectName("plainTextEdit_17")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(340, 350, 141, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.plainTextEdit_18 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_18.setGeometry(QtCore.QRect(720, 510, 121, 21))
        self.plainTextEdit_18.setObjectName("plainTextEdit_18")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(490, 470, 191, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(490, 490, 191, 16))
        self.label_24.setObjectName("label_24")
        self.plainTextEdit_19 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_19.setGeometry(QtCore.QRect(720, 490, 121, 21))
        self.plainTextEdit_19.setObjectName("plainTextEdit_19")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(490, 510, 191, 16))
        self.label_25.setObjectName("label_25")
        self.plainTextEdit_20 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_20.setGeometry(QtCore.QRect(720, 470, 121, 21))
        self.plainTextEdit_20.setObjectName("plainTextEdit_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 301, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 310, 301, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 390, 301, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 230, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 380, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(10, 170, 391, 16))
        self.label_27.setObjectName("label_27")
        self.plainTextEdit_21 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_21.setGeometry(QtCore.QRect(10, 190, 301, 31))
        self.plainTextEdit_21.setObjectName("plainTextEdit_21")
        self.plainTextEdit_22 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_22.setGeometry(QtCore.QRect(720, 150, 121, 21))
        self.plainTextEdit_22.setObjectName("plainTextEdit_22")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(490, 150, 191, 16))
        self.label_28.setObjectName("label_28")
        self.plainTextEdit_23 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_23.setGeometry(QtCore.QRect(720, 170, 121, 21))
        self.plainTextEdit_23.setObjectName("plainTextEdit_23")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(490, 170, 191, 16))
        self.label_29.setObjectName("label_29")
        self.plainTextEdit_24 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_24.setGeometry(QtCore.QRect(720, 320, 121, 21))
        self.plainTextEdit_24.setObjectName("plainTextEdit_24")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(490, 320, 191, 16))
        self.label_30.setObjectName("label_30")
        self.plainTextEdit_25 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_25.setGeometry(QtCore.QRect(10, 280, 71, 21))
        self.plainTextEdit_25.setObjectName("plainTextEdit_25")
        self.plainTextEdit_26 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_26.setGeometry(QtCore.QRect(80, 280, 71, 21))
        self.plainTextEdit_26.setObjectName("plainTextEdit_26")
        self.plainTextEdit_27 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_27.setGeometry(QtCore.QRect(170, 280, 71, 21))
        self.plainTextEdit_27.setObjectName("plainTextEdit_27")
        self.plainTextEdit_28 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_28.setGeometry(QtCore.QRect(240, 280, 71, 21))
        self.plainTextEdit_28.setObjectName("plainTextEdit_28")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(10, 249, 321, 31))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(10, 330, 331, 31))
        self.label_33.setObjectName("label_33")
        self.plainTextEdit_29 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_29.setGeometry(QtCore.QRect(10, 360, 71, 21))
        self.plainTextEdit_29.setObjectName("plainTextEdit_29")
        self.plainTextEdit_30 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_30.setGeometry(QtCore.QRect(80, 360, 71, 21))
        self.plainTextEdit_30.setObjectName("plainTextEdit_30")
        self.plainTextEdit_31 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_31.setGeometry(QtCore.QRect(170, 360, 71, 21))
        self.plainTextEdit_31.setObjectName("plainTextEdit_31")
        self.plainTextEdit_32 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_32.setGeometry(QtCore.QRect(240, 360, 71, 21))
        self.plainTextEdit_32.setObjectName("plainTextEdit_32")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(10, 410, 361, 31))
        self.label_34.setObjectName("label_34")
        self.plainTextEdit_33 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_33.setGeometry(QtCore.QRect(10, 440, 71, 21))
        self.plainTextEdit_33.setObjectName("plainTextEdit_33")
        self.plainTextEdit_34 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_34.setGeometry(QtCore.QRect(120, 440, 71, 21))
        self.plainTextEdit_34.setPlainText("")
        self.plainTextEdit_34.setObjectName("plainTextEdit_34")
        self.plainTextEdit_35 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_35.setGeometry(QtCore.QRect(240, 440, 71, 21))
        self.plainTextEdit_35.setObjectName("plainTextEdit_35")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(10, 460, 361, 31))
        self.label_35.setObjectName("label_35")
        self.plainTextEdit_36 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_36.setGeometry(QtCore.QRect(10, 490, 71, 21))
        self.plainTextEdit_36.setObjectName("plainTextEdit_36")
        self.plainTextEdit_37 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_37.setGeometry(QtCore.QRect(240, 490, 71, 21))
        self.plainTextEdit_37.setObjectName("plainTextEdit_37")
        self.plainTextEdit_38 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_38.setGeometry(QtCore.QRect(120, 490, 71, 21))
        self.plainTextEdit_38.setPlainText("")
        self.plainTextEdit_38.setObjectName("plainTextEdit_38")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Convertisseur de coordonnées. Fait Par Walid Hamdoun"))
        self.label_2.setText(_translate("MainWindow", "Conversion à partir d\'un fichier."))
        self.label_3.setText(_translate("MainWindow", "Souhaitez-vous convertir les coordonnées à partir d\'un fichier ? "))
        self.label_4.setText(_translate("MainWindow", "Si oui, merci de bien vouloir entrer le nom du fichier ci-dessous. "))
        self.label_5.setText(_translate("MainWindow", "Quel type de conversion voulez-vous faire ?"))
        self.radioButton_3.setText(_translate("MainWindow", "Conversion simple :"))
        self.label_6.setText(_translate("MainWindow", "Entrez le système de départ."))
        self.label_7.setText(_translate("MainWindow", "Entrez le système de sortie."))
        self.label_8.setText(_translate("MainWindow", "Coordonnées X :"))
        self.label_9.setText(_translate("MainWindow", "Coordonnées Y :"))
        self.label_10.setText(_translate("MainWindow", "Conversion directe"))
        self.label_11.setText(_translate("MainWindow", "Entrez le système de sortie."))
        self.label_12.setText(_translate("MainWindow", "Entrez le système de départ."))
        self.label_13.setText(_translate("MainWindow", "Coordonnées Y :"))
        self.label_14.setText(_translate("MainWindow", "Coordonnées X :"))
        self.radioButton_4.setText(_translate("MainWindow", "Conversion 14 param :"))
        self.label_15.setText(_translate("MainWindow", "Coordonnées Z :"))
        self.label_16.setText(_translate("MainWindow", "Time d\'acquisition (tt) :"))
        self.label_17.setText(_translate("MainWindow", "Datum ECEF :"))
        self.label_18.setText(_translate("MainWindow", "Proj LLA :"))
        self.label_19.setText(_translate("MainWindow", "ELLPS ECEF :"))
        self.label_20.setText(_translate("MainWindow", "Datum LLA :"))
        self.label_21.setText(_translate("MainWindow", "Proj ECEF : "))
        self.label_22.setText(_translate("MainWindow", "ELLPS LLA :"))
        self.radioButton_5.setText(_translate("MainWindow", "Conversion ECEF LLA:"))
        self.label_23.setText(_translate("MainWindow", "Coordonnées X :"))
        self.label_24.setText(_translate("MainWindow", "Coordonnées Y :"))
        self.label_25.setText(_translate("MainWindow", "Coordonnées Z :"))
        self.pushButton_3.setText(_translate("MainWindow", "Conversion Simple à partir d\'un fichier : GO !"))
        self.pushButton_4.setText(_translate("MainWindow", "Conversion 14 param à partir d\'un fichier : GO !"))
        self.pushButton_5.setText(_translate("MainWindow", "Conversion ECEF LLA à partir d\'un fichier : GO !"))
        self.pushButton_6.setText(_translate("MainWindow", "GO !"))
        self.pushButton_7.setText(_translate("MainWindow", "GO !"))
        self.pushButton_8.setText(_translate("MainWindow", "GO !"))
        self.label_27.setText(_translate("MainWindow", "Et le séparateur des valeurs, écrire par exemple : \"point-virgule\""))
        self.label_28.setText(_translate("MainWindow", "Toujours XY ? (True si oui) :"))
        self.label_29.setText(_translate("MainWindow", "Direction (ex : FORWARD) :"))
        self.label_30.setText(_translate("MainWindow", "Direction (ex : FORWARD) :"))
        self.label_32.setText(_translate("MainWindow", "En ordre : sys Entrée / sys Sortie / Toujours XY ? / Direction"))
        self.label_33.setText(_translate("MainWindow", "En ordre : sys Entrée / sys Sortie / Temps d\'acquisition / Direction"))
        self.label_34.setText(_translate("MainWindow", "En ordre : Proj ECEF / ELLPS ECEF / Datum ECEF"))
        self.label_35.setText(_translate("MainWindow", "En ordre : Proj LLA / ELLPS LLA / Datum LLA"))

    #---------- CONNECTION BUTTONS / FONCTIONS / START ----------#

        self.pushButton_3.clicked.connect(self.c_simple_file)
        self.pushButton_4.clicked.connect(self.c_quato_file)
        self.pushButton_5.clicked.connect(self.c_GEOcrs_file)
        self.pushButton_8.clicked.connect(self.c_simple_unique)
        self.pushButton_6.clicked.connect(self.c_quato_unique)
        self.pushButton_7.clicked.connect(self.c_GEOcrs_unique)

    #---------- CONNECTION BUTTONS / FONCTIONS / END ----------#

    #---------- BUTTONS DEFINITIONS ALPHA / START ----------#

    #---------- START OF FILE SYSTEMS ----------#

    def c_simple_file(self):
        """
        Le fichier doit suivre la disposition suivante :
        File should follow the following disposition :
        Eg:
        x;y
        -80;70
        -20;40
        ...
        ";" peut être remplacé par ",".
        ";" can be replaced with ",".
        """
        
        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        inProj = self.plainTextEdit_25.toPlainText()
        outProj = self.plainTextEdit_26.toPlainText()
        alwaysxy  = self.plainTextEdit_27.toPlainText()
        if alwaysxy == "True":
            alwaysxy == True
        direction_pos = self.plainTextEdit_28.toPlainText()
        
        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertCRScoords_Unic(inProj, outProj, row["x"], row["y"], alwaysxy, direction_pos)
            print(coords_conv)

    def c_quato_file(self):
        """
        Le fichier doit suivre la disposition suivante :
        File should follow the following disposition :
        Eg:
        x;y;z
        4213551.1590;162494.2700;4769661.5530
        4213551.1590;162494.2700;4769661.5530
        ...
        ";" peut être remplacé par ",".
        ";" can be replaced by ","
        """

        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        inProj = self.plainTextEdit29.toPlainText()
        outProj = self.plainTextEdit30.toPlainText()
        time_acquisition = self.plainTextEdit_30.toPlainText()
        direction_pos = self.toplainTextEdit_31.toPlainText()
        
        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertCRScoords_Quato(inProj, outProj, row["x"], row["y"], row["z"], time_acquisition, direction_pos)
            print(coords_conv)

    def c_GEOcrs_file(self):
        """"
        Le fichier doit suivre la disposition suivante :
        File should follow the following disposition :
        Eg:
        x;y;z
        4213551.1590;162494.2700;4769661.5530
        4213551.1590;162494.2700;4769661.5530
        ...
        ";" peut être remplacé par ",".
        ";" can be replaced by ",".
        """

        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        proj_ecef = self.toPlainTextEdit_33.toPlainText()
        ellps_ecef = self.toPlainText_34.toPlainText()
        datum_ecef = self.toPlainText_35.toPlainText()
        proj_lla = self.toPlainText_36.toPlainText()
        ellps_lla = self.toPlainText_38.toPlainText()
        datum_lla = self.toPlainText_37.toPlainText()

        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertGeoCRScoords(proj_ecef, ellps_ecef, datum_ecef, proj_lla, ellps_lla, datum_lla, row["x"], row["y"], row["z"])
            print(coords_conv)
    
    #---------- END OF FILE SYSTEMS ----------#

    #---------- START OF UNIQUE SYSTEMS ----------#
    
    def c_simple_unique(self):
        inProj = self.plainTextEdit_2.toPlainText()
        outProj = self.plainTextEdit_3.toPlainText()
        x = float(self.plainTextEdit_4.toPlainText())
        y = float(self.plainTextEdit_5.toPlainText())
        alwaysxy = self.plainTextEdit_22.toPlainText()
        if alwaysxy == "True":
            alwaysxy = True
        direction_pos = self.plainTextEdit_23.toPlainText()

        coords_conv = convertCRScoords_Unic(inProj, outProj, x, y, alwaysxy, direction_pos)
        print(coords_conv)

    def c_quato_unique(self):
        inProj = float(self.plainTextEdit_6.toPlainText())
        outProj = float(self.plainTextEdit_9.toPlainText())
        x = float(self.plainTextEdit_8.toPlainText())
        y = float(self.plainTextEdit_7.toPlainText())
        z = float(self.plainTextEdit_10.toPlainText())
        time_zone = float(self.plainTextEdit_11.toPlainText())
        direction_pos = self.plainTextEdit_24.toPlainText()

        coords_conv = convertCRScoords_Quato(inProj, outProj, x, y, z, time_zone, direction_pos)
        print(coords_conv)

    def c_GEOcrs_unique(self):
        proj_ecef = self.plainTextEdit_13.toPlainText()
        ellps_ecef = self.plainTextEdit_15.toPlainText()
        datum_ecef = self.plainTextEdit_16.toPlainText()
        proj_lla = self.plainTextEdit_14.toPlainText()
        ellps_lla = self.plainTextEdit_12.toPlainText()
        datum_lla = self.plainTextEdit_17.toPlainText()
        x = float(self.plainTextEdit_20.toPlainText())
        y = float(self.plainTextEdit_19.toPlainText())
        z = float(self.plainTextEdit_18.toPlainText())

        coords_conv = convertGeoCRScoords(proj_ecef, ellps_ecef, datum_ecef, proj_lla, ellps_lla, datum_lla, x, y, z)
        print(coords_conv)

    #---------- END OF UNIQUE SYSTEMS ----------#

    #---------- BUTTONS DEFINITIONS ALPHA / END ----------#

    #---------- ERROR PRINTING ----------#

    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook 
    
    #---------- ERROR PRINTING ----------#


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
