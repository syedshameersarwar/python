import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InterestCalculator(QDialog):

    def __init__(self,parent=None):
        super(InterestCalculator,self).__init__(parent)
        self.principalLabel = QLabel('Principal: ')
        self.principalValue = QDoubleSpinBox()
        self.principalValue.setRange(0.00,10000000)
        self.principalValue.setValue(1.00)
        self.principalValue.setPrefix('$ ')
        self.rateLabel = QLabel('Rate: ')
        self.rateValue = QDoubleSpinBox()
        self.rateValue.setRange(0.00,100)
        self.rateValue.setValue(1.00)
        self.rateValue.setSuffix(' %')
        self.yearsLabel = QLabel('Years: ')
        self.yearsValue = QComboBox()
        self.yearsValue.addItems([str(x) + ' years' for x in range(1,26)])
        self.AmountLabel = QLabel('Amount')
        self.AmountValue = QLabel()
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.principalLabel,0,0)
        gridLayout.addWidget(self.principalValue,0,1)
        gridLayout.addWidget(self.rateLabel,1,0)
        gridLayout.addWidget(self.rateValue,1,1)
        gridLayout.addWidget(self.yearsLabel,2,0)
        gridLayout.addWidget(self.yearsValue,2,1)
        gridLayout.addWidget(self.AmountLabel,3,0)
        gridLayout.addWidget(self.AmountValue,3,1)
        self.setLayout(gridLayout)
        self.connect(self.principalValue,SIGNAL('valueChanged(double)')\
                                                    ,self.updateUI)
        self.connect(self.rateValue,SIGNAL('valueChanged(double)')\
                                                    ,self.updateUI)
        self.connect(self.yearsValue,SIGNAL('currentIndexChanged(int)')\
                                                    ,self.updateUI)
        self.setWindowTitle('Interest')
        self.updateUI()

    def updateUI(self):
        principal = float(self.principalValue.value())
        rate = float(self.rateValue.value())
        year = self.yearsValue.currentIndex()+1
        amount = principal*((1+(rate/100.0))**year)
        self.AmountValue.setText('$ %.2f'%amount)


if __name__=='__main__':
    app = QApplication(sys.argv)
    interestCalculator = InterestCalculator()
    interestCalculator.show()
    app.exec_()
        
        
        
