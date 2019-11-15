import sys
import urllib.request
from bs4 import BeautifulSoup
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CurrencyConverter(QDialog):
    
    def __init__(self,parent=None):
        super(CurrencyConverter,self).__init__(parent)
        date = self.getData()
        self.atDate = QLabel(date)
        rates_list = [rate for rates in sorted(self.rates.keys())]
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates_list)
        self.fromValue = QDoubleSpinBox()
        self.fromValue.setRange(0.01,100000000)
        self.fromValue.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates_list)
        self.toValue = QLabel(1.00)
        layout = QGridLayout()
        layout.addWidget(self.atDate,0,0)
        layout.addWidget(self.fromComboBox,1,0)
        layout.addWidget(self.fromValue,1,1)
        layout.addWidget(self.toComboBox,2,0)
        layout.addWidget(self.toValue,2,1)
        self.setLayout(layout)
        self.connect(self.fromComboBox,SIGNAL('currentIndexChanged(int)'),self.update_UI)
        self.connect(self.toComboBox,SIGNAL('currentIndexChanged(int)'),self.update_UI)
        self.connect(self.fromValue,SIGNAL('valueChanged(double)'),self.update_UI)
        self.setWindowTitle('Currency Converter')


    def update_UI(self):
        from_ = str(self.fromComboBox.currentText())
        to = str(self.toComboBox.currentText())
        amount = (self.rates[from_]/self.rates[to])*self.fromValue.value()
        self.toValue.setText('%.6f'%amount)


    def getData(self):
        
        try:
            date = "Unknown"
            self.rates = {}
            web_source = 'https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/'
            web_page = urllib.request.urlopen(web_source)
            soup = BeautifulSoup(web_page,'html.parser')
            currency_head = soup.find('thead',attrs = {'class':'bocss-table__thead'})
            rowsCurrencyHead = currency_head.find_all('tr')
            for row in rowsCurrencyHead:
                cols = row.find_all('th')
                cols = [ col.text.strip() for col in cols ]
                date = str(cols[-1])
            currency_table = soup.find('tbody',attrs = {'class':'bocss-table__tbody'})
            rows = currency_table.find_all('tr',attrs = {'class':'bocss-table__tr'})
            for row in rows:
                currency_name = row.find_all('th')
                rates = row.find_all('td')
                currency_name = [name.text.strip() for name in currency_name]
                rates = [rate.text.strip() for rate in rates]
                self.rates[str(currency_name[0])]= float(rates[-1])
            return "Exchange Rates Date: "+date
        except Exception as e:
            return "Failed to Download:\n%s" % e


if __name__=='__main__':
    app = QApplication(sys.argv)
    Currency_Converter = CurrencyConverter()
    Currency_Converter.show()
    app.exec_()
                
