
from PyQt5.QtWidgets import QWidget,QLabel,QMainWindow,QTextEdit,QTextBrowser,QApplication,QVBoxLayout,QPushButton,QPlainTextEdit,QLineEdit,QComboBox,QHBoxLayout
import requests

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.main_ui()
        self.api_data_al()


    def main_ui(self):

        self.tur = QComboBox()
        self.tur.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.miktar = QLineEdit("Lütfen Bu alana Euro Cinsinden miktarınızı giriniz")
        self.buton2 = QPushButton("Çevir")
        self.sonuc = QLineEdit()
        self.sonuc.setReadOnly(True)

        self.miktar.setClearButtonEnabled(True)
        self.tur.setStyleSheet("QComboBox"
                                     "{"
                                     "padding-left: 360;"
                                     "font-size: 25px;" 
                                     "background-color: #008CBA;"
                                     "color:white;" 
                                     "}")

        self.miktar.setStyleSheet("QLineEdit"
                                     "{"
                                     "font-size: 25px;"
                                     "background-color: white;"  
                                     "}")

        self.buton2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: white;font-size: 25px;}')

        self.sonuc.setStyleSheet("QLineEdit"
                                  "{"
                                  "font-size: 25px;"
                                  "background-color: white;"
                                  "}")


        v_box = QVBoxLayout()
        v_box.addWidget(self.miktar)
        v_box.addWidget(self.tur)
        v_box.addWidget(self.buton2)
        v_box.addWidget(self.sonuc)
        v_box.addStretch()

        h_box = QHBoxLayout()

        h_box.addLayout(v_box)



        self.setLayout(h_box)

        self.buton2.clicked.connect(lambda : self.cevir(self.miktar.text(),self.tur.currentText()))
        self.setGeometry(800,200,800,200)
        self.setWindowTitle("Exchange")
        self.setStyleSheet("background-color: #464956;")
        self.show()

    def api_data_al(self):
        api_key = "577312f59f16d3a338ee4c38f3ffb7a9"
        self.url = "http://api.exchangeratesapi.io/v1/latest?access_key=" + api_key
        request = requests.get(self.url)
        json_verisi = request.json()
        json_verisi = json_verisi["rates"]


        for row in json_verisi:
            self.tur.addItem(row)




    def cevir(self,miktar,tur):
        self.newUrl = self.url + "&" +tur
        request = requests.get(self.newUrl)
        json_verisi = request.json()
        sonuc = json_verisi["rates"][tur]
        sonuc = float(miktar) * float(sonuc)
        self.sonuc.setText(str(sonuc))

