from PySide2.QtCore import *
import sys
from PySide2.QtWidgets import *
from ui_converterpage import Ui_MainWindow as mainScreen
from circularprogressbar import CircularSplashScreen as splashscreen
from ui_circularProgressBar import Ui_MainWindow

counter = 0

class Speaker():
    def __init__(self,text,voice):

        import pyttsx3
        self.finished = Signal()
        self.start = Signal()
        engine = pyttsx3.init('sapi5')

        if voice == "male":
            setvoice = engine.getProperty('voices')[0].id
        else :
            setvoice = engine.getProperty('voices')[1].id

        engine.setProperty('voice', setvoice)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        engine.say(text)
        engine.runAndWait()
        self.finished.emit()



class MyApplication(QMainWindow):
    """Main UI screen Class """
    def __init__(self):
        super().__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)
        self.splashscreen = splashscreen()
        self.ui.buttonspeak.clicked.connect(self.speakfunction)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.Minimizebtn.clicked.connect(self.mini)
        self.ui.CloseButton.clicked.connect(self.closer)



        def moveWindow(e):
            FRAME = QApplication.desktop().screenGeometry()
            if not (FRAME == self.geometry()):
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.TitleBar.mouseMoveEvent = moveWindow

        self.oldgeo = self.geometry()

    def maxi(self):
        fullscreen = QApplication.desktop().screenGeometry() == self.geometry()

        if fullscreen :
            self.setGeometry(self.oldgeo)
        else:
            self.setGeometry(QApplication.desktop().screenGeometry())

    def closer(self):
        self.close()

    def mini(self):
        self.showMinimized()

    def mousePressEvent(self, event) -> None:
        self.clickPosition = event.globalPos()

    def speakfunction(self):
        """Function for Pyttsx3 to speak a sentence or words"""
        text = self.ui.textbox.text()
        self.ui.textbox.clear()
        import pyttsx3
        engine = pyttsx3.init('sapi5')

        if self.ui.DavidButton.isChecked():
            setvoice = engine.getProperty('voices')[0].id

        elif self.ui.ZiraButton.isChecked():
            setvoice = engine.getProperty('voices')[1].id

        engine.setProperty('voice',setvoice)
        engine.setProperty('rate',150)
        engine.setProperty('volume',1)

        def say(line):
            engine.say(line)
            engine.runAndWait()

        say(text)


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
        self.timer.start(5)

        self.show()

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
            self.main = MyApplication()
            self.main.show()


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



if __name__ == '__main__':
    app = QApplication()
    window = CircularSplashScreen()
    sys.exit(app.exec_())