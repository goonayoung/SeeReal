import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QComboBox
, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLineEdit, QLabel, QTableWidget)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.setSetting())
        #vbox.addWidget(self.setInput())
        #vbox.addWidget(self.setOutput())

        self.setLayout(vbox)

        self.setWindowTitle('KAI Testcase Recommandation Program')
        self.resize(700,800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setSetting(self):
        groupbox = QGroupBox('Setting')

        groupbox1 = QGroupBox('검색 범위')
        groupbox1.setFlat(True)
        groupbox2 = QGroupBox('결과 갯수')
        groupbox2.setFlat(True)
        groupbox1.setCheckable(True)
        groupbox1.setChecked(False)
        groupbox2.setCheckable(True)
        groupbox2.setChecked(False)

        self.cb1 = QComboBox(self)
        self.cb1.addItem('3.2.11')
        self.cb1.addItem('3.2.12')
        self.cb1.addItem('3.2.13')
        self.cb1.addItem('3.2.14')
        label1 = QLabel('~',self)
        
        self.cb2 = QComboBox(self)
        self.cb2.addItem('3.2.11')
        self.cb2.addItem('3.2.12')
        self.cb2.addItem('3.2.13')
        self.cb2.addItem('3.2.14')
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.cb1)
        hbox1.addWidget(label1)
        hbox1.addWidget(self.cb2)
        groupbox1.setLayout(hbox1)

       
        self.qle3 = QLineEdit(self)
        label2 = QLabel('개',self)
        self.qle3.setText('1')
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.qle3)
        hbox2.addWidget(label2)
        groupbox2.setLayout(hbox2)

        btn = QPushButton('Set',self)
        btn.setCheckable(True)
        btn.clicked.connect(self.setClicked)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox1)
        hbox.addWidget(groupbox2)
        hbox.addStretch(1)
        hbox.addWidget(btn)
        groupbox.setLayout(hbox)

        return groupbox

    def setClicked(self):
        print('Set')
        self.cb1.currentTextChanged.connect(self.setClicked)
        self.cb2.currentTextChanged.connect(self.setClicked)
        self.SearchR1 = self.cb1.currentText()
        self.SearchR2 = self.cb2.currentText()
        print("Search Range1 is : " ,self.SearchR1)
        print("Search Range2 is : ", self.SearchR2)
        self.outputnum = int(self.qle3.text())
        print("outputnum is : " , self.outputnum)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())