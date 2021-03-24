from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
from ui_circularProgressBar import Ui_MainWindow

counter = 0
class CircularSplashScreen(QMainWindow):
    def __init__(self):
        super(CircularSplashScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ProgressBarValue(2)

        self.timer = QTimer()
        self.timer.timeout.connect(self.Progresser)
        self.timer.start(35)




    def Progresser(self):
        global counter
        from random import choice

        processingmsg = ["Searching Files","Connecting Database"]
        self.loadinHTML = f"""<html><head/><body><p align="center"><span style=" font-size:8pt;">
        {choice([choice(processingmsg),choice(processingmsg),choice(processingmsg),choice(processingmsg)] )}....
        </span></p></body></html>"""
        self.ui.LoadingLabel.setText(self.loadinHTML)

        self.ProgressBarValue(counter)
        self.html = ''' <html><head/><body><p align="center"><span style=" font-size:72pt;
         font-weight:600;">{VALUE}</span><span style=" font-size:24pt; vertical-align:super;">%</span></p></body></html> '''
        self.html = self.html.replace('{VALUE}',str(counter) )

        self.ui.PercentLabel.setText(self.html)

        if counter>=100:
            self.timer.stop()
            self.ProgressBarValue(100)
            self.ui.PercentLabel.setText(''' <html><head/><body><p align="center"><span style=" font-size:72pt;
         font-weight:600;">100</span><span style=" font-size:24pt; vertical-align:super;">%</span></p></body></html> ''')

            self.ui.LoadingLabel.setText('<html><head/><body><p align="center"><span style=" font-size:8pt;">Done!</span></p></body></html>')
            # counter = 0

            self.timer.stop()
            self.close()


        counter+= 1

    def ProgressBarValue(self,value):

        stylesheet = """
    QLabel{
border-radius:150px;
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 53, 53, 0), stop:{STOP_2} rgba(255, 245, 53, 255));
}"""
        progress = (100 - value) / 100.00
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        # widget.setStyleSheet(newStylesheet)
        self.ui.ProgressBar.setStyleSheet(newStylesheet)

def main():
    app = QApplication()
    window = CircularSplashScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
