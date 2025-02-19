# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("PyQt5/Bro_Code.webp"))

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("PyQt5/Bro_Code.webp")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        # label.setGeometry(self.width() - label.width(), 
        #                   0, 
        #                   label.width(), 
        #                   label.height()) # TOP RIGHT CORNER


        # label.setGeometry(self.width() - label.width(), 
        #                   self.height() - label.height(), 
        #                   label.width(), 
        #                   label.height()) # BOTTOM RIGHT CORNER

        # label.setGeometry(0, 
        #                   self.height() - label.height(), 
        #                   label.width(), 
        #                   label.height()) # BOTTOM LEFT CORNER

        label.setGeometry((self.width() - label.width()) // 2, 
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height()) # MIDDLE

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()