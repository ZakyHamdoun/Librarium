# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from fonc import convertCRScoords_Unic, convertCRScoords_Quato, convertGeoCRScoords

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
        self.label_4.setGeometry(QtCore.QRect(10, 120, 301, 16))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 140, 301, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 50, 291, 16))
        self.label_5.setObjectName("label_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 70, 121, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 70, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 90, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 110, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 130, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 30, 181, 16))
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(670, 70, 121, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(670, 90, 121, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(670, 110, 121, 21))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(670, 130, 121, 21))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(490, 220, 141, 16))
        self.label_11.setObjectName("label_11")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(670, 200, 121, 21))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 200, 141, 16))
        self.label_12.setObjectName("label_12")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(670, 260, 121, 21))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(490, 260, 81, 16))
        self.label_13.setObjectName("label_13")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(670, 240, 121, 21))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(490, 240, 91, 16))
        self.label_14.setObjectName("label_14")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(670, 220, 121, 21))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(360, 200, 131, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(490, 280, 81, 16))
        self.label_15.setObjectName("label_15")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(670, 280, 121, 21))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(490, 300, 81, 16))
        self.label_16.setObjectName("label_16")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(670, 300, 121, 21))
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(670, 430, 121, 21))
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(490, 390, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(490, 410, 81, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(490, 370, 141, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(490, 450, 81, 16))
        self.label_20.setObjectName("label_20")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(670, 350, 121, 21))
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.plainTextEdit_14 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_14.setGeometry(QtCore.QRect(670, 410, 121, 21))
        self.plainTextEdit_14.setObjectName("plainTextEdit_14")
        self.plainTextEdit_15 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_15.setGeometry(QtCore.QRect(670, 370, 121, 21))
        self.plainTextEdit_15.setObjectName("plainTextEdit_15")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(490, 350, 141, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(490, 430, 81, 16))
        self.label_22.setObjectName("label_22")
        self.plainTextEdit_16 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_16.setGeometry(QtCore.QRect(670, 390, 121, 21))
        self.plainTextEdit_16.setObjectName("plainTextEdit_16")
        self.plainTextEdit_17 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_17.setGeometry(QtCore.QRect(670, 450, 121, 21))
        self.plainTextEdit_17.setObjectName("plainTextEdit_17")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(360, 350, 131, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.plainTextEdit_18 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_18.setGeometry(QtCore.QRect(670, 510, 121, 21))
        self.plainTextEdit_18.setObjectName("plainTextEdit_18")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(490, 470, 91, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(490, 490, 81, 16))
        self.label_24.setObjectName("label_24")
        self.plainTextEdit_19 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_19.setGeometry(QtCore.QRect(670, 490, 121, 21))
        self.plainTextEdit_19.setObjectName("plainTextEdit_19")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(490, 510, 81, 16))
        self.label_25.setObjectName("label_25")
        self.plainTextEdit_20 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_20.setGeometry(QtCore.QRect(670, 470, 121, 21))
        self.plainTextEdit_20.setObjectName("plainTextEdit_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 301, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 250, 301, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 270, 301, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 230, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 380, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 100, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(10, 300, 311, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(10, 170, 301, 16))
        self.label_27.setObjectName("label_27")
        self.plainTextEdit_21 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_21.setGeometry(QtCore.QRect(10, 190, 301, 31))
        self.plainTextEdit_21.setObjectName("plainTextEdit_21")
        self.plainTextEdit_22 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_22.setGeometry(QtCore.QRect(670, 150, 121, 21))
        self.plainTextEdit_22.setObjectName("plainTextEdit_22")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(490, 150, 141, 16))
        self.label_28.setObjectName("label_28")
        self.plainTextEdit_23 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_23.setGeometry(QtCore.QRect(670, 170, 121, 21))
        self.plainTextEdit_23.setObjectName("plainTextEdit_23")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(490, 170, 141, 16))
        self.label_29.setObjectName("label_29")
        self.plainTextEdit_24 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_24.setGeometry(QtCore.QRect(670, 320, 121, 21))
        self.plainTextEdit_24.setObjectName("plainTextEdit_24")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(490, 320, 141, 16))
        self.label_30.setObjectName("label_30")
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
        self.label_4.setText(_translate("MainWindow", "Si oui, merci de bien vouloir entrer le nom du fichier ci-dessous. Notez que le fichier doit se trouver dans le même répertoire."))
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
        self.label_16.setText(_translate("MainWindow", "Time Zone :"))
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
        self.label_26.setText(_translate("MainWindow", "Exemple : Nom : coords.csv / Séparateur : \";\""))
        self.label_27.setText(_translate("MainWindow", "Et le séparateur des valeurs, écrire par exemple : \";\""))
        self.label_28.setText(_translate("MainWindow", "Toujours XY ? (True si oui) :"))
        self.label_29.setText(_translate("MainWindow", "Direction (ex : FORWARD) :"))
        self.label_30.setText(_translate("MainWindow", "Direction (ex : FORWARD) :"))

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
        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        
        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertCRScoords_Unic(row["inProj"], row["outProj"], row["x"], row["y"], row["alwaysxy"], row["direction_pos"])
            print(coords_conv)

    def c_quato_file(self):
        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        
        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertCRScoords_Quato(row["inProj"], row["outProj"], row["x"], row["y"], row["z"], row["time_zone"], row["direction_pos"])
            print(coords_conv)

    def c_GEOcrs_file(self):
        fichier = self.plainTextEdit.toPlainText()
        sep_valeurs = self.plainTextEdit_21.toPlainText()
        
        if sep_valeurs == "point-virgule":
            coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
        if sep_valeurs == "virgule":
            coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.
        for index, row in coords.iterrows():
            coords_conv = convertGeoCRScoords(row["proj_ecef"], row["ellps_ecef"], row["datum_ecef"], row["proj_lla"], row["ellps_lla"], row["datum_lla"], row["x"], row["y"], row["z"])
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
