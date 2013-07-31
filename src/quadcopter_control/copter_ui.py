#!/usr/bin/env python

import sys
import os
from python_qt_binding import QtCore, QtGui, loadUi
from QtGui import QMainWindow, QApplication

# NOTE: make sure the <projectRoot>/src directory
#       is in your PYTHONPATH environment variable.
#       So, when you are in the project root directory
#       on the command line, type:
#   export PYTHONPATH=./src:$PYTHONPATH

class CopterUI (QMainWindow):
    
    def __init__(self):
        # Must call init method of superclass:
        super(CopterUI, self).__init__()
        self.initUI();
        # If we don't call 'show()' we won't see anything:
        self.ui.show();
    
#    def initUI(self):
#        self.ui = loadUi("../QtFiles/qt_example/quadcopterUi.ui")
#        self.ui.testPushButton.clicked.connect(self.handleTestButton)

    def initUI(self):
        '''
        Find the QtCreator's xxx.ui file and load it to
        learn what the UI should look like:
        '''
        thisFilesLocationDir = os.path.dirname(__file__)
        qtUiFilePath = os.path.join(thisFilesLocationDir, "../QtFiles/qt_example/quadcopterUi.ui")
        self.ui = loadUi(qtUiFilePath)
        
        # Connect the clicking of the button in the UI with
        # a particular method of this class (NOTE: we pass
        # a method object to the 'connect()' method by *not* having
        # parentheses after the 'self.handleTestButton'. If we were
        # to put parens there, we'd be *calling* that method, rather
        # than specifying the method name for connect() to remember: 
        self.ui.testPushButton.clicked.connect(self.handleTestButton)


    def handleTestButton(self):
        '''
        Called whenever the test button is clicked. 
        We could do anything we like here.
        '''
        print("Test button was pushed.")
        
if __name__ == "__main__":
    # Boilerplate for all Qt applications:
    # create an application instance, create
    # an instance of our object, and go into
    # an infinite event loop. To break out of it,
    # click the 'X' button in the application's 
    # window title bar: 
    app = QApplication(sys.argv);
    myCopterUI = CopterUI();
    app.exec_();

