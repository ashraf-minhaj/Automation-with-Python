""" Full Screen Web Browser with Python

author: ashraf minhaj
mainl: ashraf_minhaj@yahoo.com
"""

"""
install -
$ pip install pyqt5
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage as QWebPage #needed
except:
    from PyQt5.QtWebKitWidgets import QWebView, QWebPage #needed

class Browser(QMainWindow):
    """
    The Browser class
    """
    def __init__(self, *args, **kwargs):
        """ init runs when a class is called, ever. 
        it is a must to have """
        super(Browser, self).__init__(*args, **kwargs)

        self.web = QWebView.__init__(self)   #initialize qwebview
        self.ui()  # run the UI

    def ui(self):
        """ this function will bear all the things of our UI"""
        self.setWindowTitle("My Browser")

        # we will place things in a grid layout
        my_layout = QGridLayout()

        self.search_box = QLineEdit(self)
        self.search_box.setStyleSheet("background-color: white; color: black; border-radius : 5; border: 1px solid white")
        self.search_box.setPlaceholderText(" search")
        self.search_box.setFont(QFont('SimHei', 10, 10))
        self.search_box.setText("http://")                        # text to help you out with the url

        self.go_button = QPushButton(self)
        self.go_button.setText(" GO ")
        self.go_button.setStyleSheet("Background-color: black; color: white; border-style: outset;  border-radius : 5; border: 1px solid white")
        self.go_button.setFont(QFont('SimHei', 10, 10))
        self.go_button.clicked.connect(lambda : self.web.load(QUrl(self.search_box.text())))

        # bookmark buttons
        self.fb = QPushButton(self)
        self.fb.setText("fb")
        self.fb.clicked.connect(lambda : self.go(url='http://facebook.com'))

        self.yt = QPushButton(self)
        self.yt.setText("YT")
        self.yt.clicked.connect(lambda : self.go(url='http://youtube.com'))

        self.news = QPushButton(self)
        self.news.setText("News")
        self.news.clicked.connect(lambda : self.go(url='http://prothom-alo.com'))

        self.fav = QPushButton(self)
        self.fav.setText("Fav")
        self.fav.clicked.connect(lambda : self.go(url='http://programming-hero.com'))

        # webview to show webpages
        self.web = QWebView(self)
        self.web.load(QUrl("http://google.com"))

        # add everything in the layout
        my_layout.addWidget(self.fb, 0, 0)
        my_layout.addWidget(self.search_box, 0, 1)
        my_layout.addWidget(self.go_button, 0, 2)
        my_layout.addWidget(self.yt, 1, 0)
        my_layout.addWidget(self.web, 1, 1, 4, 3)  # takes 4 columns and 3 rows
        my_layout.addWidget(self.news, 2, 0)
        my_layout.addWidget(self.fav, 3, 0)

        widget = QWidget()
        widget.setLayout(my_layout)
        self.setCentralWidget(widget)
        
        #self.show()          # make the UI visible
        self.showMaximized() # show the window in fullscreen

    def go(self, url):
        #url = self.search_box.text()
        print(url)
        self.search_box.setText(url)
        self.web.load(QUrl(url))


# run the browser
app = QApplication(sys.argv)
window = Browser()

#start event loop
app.exec_()