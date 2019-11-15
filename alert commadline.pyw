import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

try:
    due_time = QTime.currentTime()
    message = "Alert! "
    if len(sys.argv)<2:
        raise ValueError
    (hours,minutes) = sys.argv[1].split[":"]
    due_time = QTime(int(hours),int(minutes))
    if not due_time.isValid():
        raise ValueError
    message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]."

while QTime.currentTime()<due_time:
    time.sleep(20)
    
label = QLabel("<font color = blue size = 75><b> "+message+"</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000,app.quit)
app.exec_()
