import sys
import SeeReal_KAI_
import unittest

from PyQt5.QtWidgets import (QApplication, QTableWidgetItem)
app= QApplication( sys.argv )

class TestCase2(unittest.TestCase):
    def setup(self):
        pass
    
    def test_Search_clicked(self):
        a = SeeReal_KAI_.MyApp()
        
        inputTable1 = 'Input Source'
        inputTable2 = 'Signal Description'
        inputTable3 = 'Type'
        inputTable4 = '1234'
        
        a.table.setItem(0, 0, QTableWidgetItem(inputTable1))
        a.table.setItem(0, 1, QTableWidgetItem(inputTable2))
        a.table.setItem(0, 2, QTableWidgetItem(inputTable3))
        a.table.setItem(0, 3, QTableWidgetItem(inputTable4))
        
        a.setBtn.click()
        a.searchBtn.click()
         
        self.assertEqual(a.testInput1, inputTable1)
        self.assertEqual(a.testInput2, inputTable2)
        self.assertEqual(a.testInput3, inputTable3)
        self.assertEqual(a.testInput4, inputTable4)

        
if __name__ == "__main__":
    unittest.main()   