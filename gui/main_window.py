import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel

# Importing the individual tab classes
from memory_tab import MemoryTab
from disk_tab import DiskTab
from email_tab import EmailTab
from network_tab import NetworkTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PORSHA - Digital Forensics Toolkit')
        self.setGeometry(400, 400, 1200, 800)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Adding tabs
        self.tab_widget.addTab(MemoryTab(), 'Memory Analysis')
        self.tab_widget.addTab(DiskTab(), 'Disk Analysis')
        self.tab_widget.addTab(EmailTab(), 'Email Analysis')
        self.tab_widget.addTab(NetworkTab(), 'Network Analysis')
      


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Macintosh')

    # Apply a custom stylesheet
    stylesheet = """
        QMainWindow {
            background-color: #f0f0f0;
        }
        QTabWidget::pane {
            border: 1px solid #ccc;
        }
        QTabBar::tab {
            background: #ccc;
            padding: 10px;
        }
        QTabBar::tab:selected {
            background: #aaa;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        QTextEdit {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
        }
    """
    app.setStyleSheet(stylesheet)
    main_window = MainWindow() 
    main_window.show()
    sys.exit(app.exec_())