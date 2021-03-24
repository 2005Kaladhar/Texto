from PySide2.QtWidgets import *
import sys
from ui_converterpage import Ui_MainWindow as screen

class LiveApp(QMainWindow):
    def __init__(self):
        super(LiveApp, self).__init__()
        self.ui = screen()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LiveApp()
    sys.exit( app.exec_() )




