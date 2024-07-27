import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget

# Importing the individual tab classes
from memory_tab import MemoryTab
from disk_tab import DiskTab
from email_tab import EmailTab
#from network_tab import NetworkTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PORSHA - Digital Forensics Toolkit')
        self.setGeometry(100, 100, 1200, 800)
        
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

               # Adding tabs
        self.tab_widget.addTab(MemoryTab(), 'Memory Analysis')
        self.tab_widget.addTab(DiskTab(), 'Disk Analysis')
        self.tab_widget.addTab(EmailTab(), 'Email Analysis')
        #self.tab_widget.addTab(NetworkTab(), 'Network Analysis')
      



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())