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
        #vbox.addWidget(self.setInput())
        vbox.addWidget(self.setOutput())

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

    def setOutput(self):
        groupbox = QGroupBox('Output')

        vbox = QVBoxLayout()
        vbox.addWidget(self.ouputTable())

        hbox = QHBoxLayout()
        btn1 = QPushButton('More')
        btn2 = QPushButton('Save')
        btn1.clicked.connect(self.moreClicked)
        btn2.clicked.connect(self.saveClicked)
        hbox.addStretch(2)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox.addLayout(hbox)

        groupbox.setLayout(vbox)

        return groupbox

    def moreClicked(self):
        print("more")
        
    def saveClicked(self):
        print("save")

    def ouputTable(self):
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