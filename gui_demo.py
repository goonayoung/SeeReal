import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QComboBox
, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLineEdit, QLabel, QTableWidget)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.Setting())
        vbox.addWidget(self.Input())
        vbox.addWidget(self.Output())

        self.setLayout(vbox)

        self.setWindowTitle('KAI Testcase Recommandation Program')
        self.resize(800,800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Setting(self):
        groupbox = QGroupBox('Setting')

        groupbox1 = QGroupBox('검색 범위')
        groupbox1.setFlat(True)
        groupbox2 = QGroupBox('결과 갯수')
        groupbox2.setFlat(True)
        groupbox1.setCheckable(True)
        groupbox1.setChecked(False)
        groupbox2.setCheckable(True)
        groupbox2.setChecked(False)

        cb1 = QComboBox(self)
        cb1.addItem('3.2.11')
        cb1.addItem('3.2.12')
        cb1.addItem('3.2.13')
        cb1.addItem('3.2.14')
        label1 = QLabel('~',self)
        cb2 = QComboBox(self)
        cb2.addItem('3.2.11')
        cb2.addItem('3.2.12')
        cb2.addItem('3.2.13')
        cb2.addItem('3.2.14')
        hbox1 = QHBoxLayout()
        hbox1.addWidget(cb1)
        hbox1.addWidget(label1)
        hbox1.addWidget(cb2)
        groupbox1.setLayout(hbox1)

        qle3 = QLineEdit(self)
        label2 = QLabel('개',self)
        qle3.setText('1')
        hbox2 = QHBoxLayout()
        hbox2.addWidget(qle3)
        hbox2.addWidget(label2)
        groupbox2.setLayout(hbox2)

        btn = QPushButton('Set',self)
        btn.setCheckable(True)
        btn.clicked.connect(self.Set_clicked)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox1)
        hbox.addWidget(groupbox2)
        hbox.addStretch(1)
        hbox.addWidget(btn)
        groupbox.setLayout(hbox)

        return groupbox

    def Set_clicked(self):
        print('Set')

    def Input(self):
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
        btn.clicked.connect(self.Search_clicked)
        hbox3.addStretch(2)
        hbox3.addWidget(btn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(Tableinputbox)
        vbox.addLayout(hbox3)

        groupbox.setLayout(vbox)
        groupbox.setFixedHeight(200)

        return groupbox

    def I_clicked(self):
        print('internal')
        self.table.clear()
        self.table.setFixedHeight(90)
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
        self.table.setFixedHeight(90)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        column_headers = ['INPUT SOURCE', 'SIGNAL DESCRIPTION', 'ICD SIGNAL SPECIFICATION']
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setColumnWidth(1, 361)
        self.table.setColumnWidth(2, 160)

    def Search_clicked(self):
        print("Search")

    def Output(self):
        groupbox = QGroupBox('Output')

        vbox = QVBoxLayout()
        vbox.addWidget(self.OuputTable())

        hbox = QHBoxLayout()
        btn1 = QPushButton('More')
        btn2 = QPushButton('Save')
        btn1.clicked.connect(self.More_clicked)
        btn2.clicked.connect(self.Save_clicked)
        hbox.addStretch(2)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox.addLayout(hbox)

        groupbox.setLayout(vbox)

        return groupbox

    def More_clicked(self):
        print("more")

    def Save_clicked(self):
        print("save")

    def OuputTable(self):
        box = QGroupBox()

        table = QTableWidget()
        table.setRowCount(1)
        table.setColumnCount(3)
        column_headers = ['Test Action', 'Expected Result', 'Pass/Fail']
        table.setHorizontalHeaderLabels(column_headers)
        table.setColumnWidth(0, 260)
        table.setColumnWidth(1, 281)
        table.setColumnWidth(2, 80)
        vbox = QVBoxLayout()
        vbox.addWidget(table)
        box.setLayout(vbox)

        return box


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())