from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit

class DiskTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        self.run_button = QPushButton('Run Disk Analysis')
        self.output_area = QTextEdit()
        
        layout.addWidget(self.run_button)
        layout.addWidget(self.output_area)
        
        self.setLayout(layout)
        
        self.run_button.clicked.connect(self.run_disk_analysis)
        
    def run_disk_analysis(self):
        self.output_area.append("Running disk analysis...")
        result = self.analyze_disk()
        self.output_area.append(result)
        
    def analyze_disk(self):
        # Placeholder for actual disk analysis logic
        return "Disk analysis complete."