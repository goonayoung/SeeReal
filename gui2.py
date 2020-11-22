import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QComboBox
, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLineEdit, QLabel, QTableWidget)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        #vbox.addWidget(self.setSetting())
        vbox.addWidget(self.setInput())
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

    def setInput(self):
        groupbox = QGroupBox('Input')

        hbox1 = QHBoxLayout()
        self.I_button = QRadioButton('Internal Input')
        self.E_button = QRadioButton('External Input')
        #self.I_button.setChecked(True)
        self.I_button.clicked.connect(self.I_clicked)
        self.E_button.clicked.connect(self.E_clicked)
        hbox1.addWidget(self.I_button)
        hbox1.addWidget(self.E_button)

        Tableinputbox = QHBoxLayout()
        self.table = QTableWidget()
        Tableinputbox.addWidget(self.table)

        hbox3 = QHBoxLayout()
        btn = QPushButton('Search')
        btn.clicked.connect(self.searchClicked)
        hbox3.addStretch(2)
        hbox3.addWidget(btn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(Tableinputbox)
        vbox.addLayout(hbox3)

        groupbox.setLayout(vbox)
        groupbox.setFixedHeight(170)

        return groupbox

    def I_clicked(self):
        print('internal')
        self.table.clear()
        self.table.setFixedHeight(55)
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        column_headers = ['INPUT SOURCE', 'SIGNAL DESCRIPTION', 'TYPE', 'PACKET ID']
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setColumnWidth(1, 361)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 80)

    def E_clicked(self):
        print('external')
        self.table.clear()
        self.table.setFixedHeight(55)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        column_headers = ['INPUT SOURCE', 'SIGNAL DESCRIPTION', 'ICD SIGNAL SPECIFICATION']
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setColumnWidth(1, 361)
        self.table.setColumnWidth(2, 160)

    def searchClicked(self):
        print("Search")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())