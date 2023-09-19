from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
app=QApplication([])
win_x, win_y = 200, 50
win_width, win_height = 1000, 600
txt_title = 'English knowledge test'
txt_hello = 'You are going to pass a test to discover your level of knowing English. There are 5 different questions.the difficulty increases with each question. \nIf you will pass the exam without any mistakes you can mark your level of knowing English as upper-intermediate. Be attentive, good luck!. In this test you may paste some letters into a words with missings'
txt_q1 = 'Which letter is missed? Rh_tm.'
txt_q2 = 'Which word must starts with capital first letter? Write a full word. river, castle, ocean, moreover, russian.'
txt_q3 = 'In which form verb "go" must be in this sentence? A am go to be a police officer.'
txt_q4 = 'Which multi-part verb is correct for this sentence? I have understood that i must give *** smoking.'
txt_q5 = 'Choose the right transcription of word choir. Write only a number. 1. [ʃɔir] 2.[kwaIə] 3.[choir] 4.[kvaeue]'
space = ''
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)  
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.text1 = QLabel(txt_q1)
        self.text2 = QLabel(txt_q2)
        self.text3 = QLabel(txt_q3)
        self.text4 = QLabel(txt_q4)
        self.text5 = QLabel(txt_q5)
        self.line1 = QLineEdit(space)
        self.line2 = QLineEdit(space)
        self.line3 = QLineEdit(space)
        self.line4 = QLineEdit(space)
        self.line5 = QLineEdit(space)
        self.ans1 = QLabel('')
        self.ans2 = QLabel('')
        self.ans3 = QLabel('')
        self.ans4 = QLabel('')
        self.ans5 = QLabel('')
        self.checkbtn = QPushButton('Check results')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.ans1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.line2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.ans2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.ans3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text4, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.ans4, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text5, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.line5, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.ans5, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.checkbtn, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)
    def connects(self):
        self.checkbtn.clicked.connect(self.result)
    def result(self):
        self.ans1.setText('y')
        self.ans2.setText('Russian')
        self.ans3.setText('going')
        self.ans4.setText('up')
        self.ans5.setText('2')
window = MainWin()
app.exec_()