from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Using QMainWindow makes setting up a layout tough

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,200)
        self.setWindowTitle("(ALPHA) AI-CRIBZ")
        #Input fields
        self.input = ""
        self.confidence = 0.5
        self.threshold = 0.3
        self.grabcut = 10
        self.radius = 3
        #Widget Init
        self.image_button = QPushButton(self)
        self.image_button.setText("Upload Image")
        self.image_button.clicked.connect(self.getImage)
        self.image_button.move(50,60)

        self.selected_image = QLabel(self)
        self.selected_image.setText("Empty")
        self.selected_image.move(150,60)
        self.selected_image.resize(200,30)
        self.selected_image.setStyleSheet("border: 1px solid black;")

        self.thresholdV = QDoubleSpinBox(self)
        self.thresholdV.setRange(0.0,1.0)
        self.thresholdV.setValue(0.3)
        self.thresholdV.setSingleStep(0.1)
        self.thresholdV.setPrefix("Threshold: ")
        self.thresholdV.move(50,20)

        self.confidenceV = QDoubleSpinBox(self)
        self.confidenceV.setRange(0.0, 1.0)
        self.confidenceV.setValue(0.5)
        self.confidenceV.setSingleStep(0.1)
        self.confidenceV.setPrefix("Confidence: ")
        self.confidenceV.move(150,20)
        self.confidenceV.resize(110,30)

        self.grabcutV = QSpinBox(self)
        self.grabcutV.setRange(1,100)
        self.grabcutV.setValue(10)
        self.grabcutV.setSingleStep(1)
        self.grabcutV.setPrefix("Grabcuts: ")
        self.grabcutV.move(260,20)

        self.radiusV = QSpinBox(self)
        self.radiusV.setRange(1,10)
        self.radiusV.setValue(3)
        self.radiusV.setSingleStep(1)
        self.radiusV.setPrefix("Radius: ")
        self.radiusV.move(360,20)

        self.submit_button = QPushButton(self)
        self.submit_button.setText("Ok")
        self.submit_button.clicked.connect(self.submitResults)
        self.submit_button.move(50, 150)
        
    def getImage(self) -> str:
        dialog = QFileDialog()
        selected, filter = dialog.getOpenFileName(None, "", filter = "Images (*.png *.xpm *.jpg)")
        print(selected, filter)
        if(len(selected) == 0):
            error = QMessageBox()
            error.setWindowTitle("ERROR: Non-Response Detected!")
            error.setText("ERROR: No input image specified, please try again.")
            error.exec_()
            return
        else:
            message = QMessageBox()
            message.setWindowTitle("Image Received")
            message.setText(str("Image Selected: " + selected))
            message.exec_()
        self.input = selected
        self.selected_image.setText(self.input)

    def submitResults(self):
        if(len(self.input) == 0):
            error = QMessageBox()
            error.setWindowTitle("Input Image Not Received")
            error.setText("ERROR: Input Image not specified, please input image first.")
            error.exec_()
            return
        self.confidence = self.confidenceV.value()
        self.threshold = self.thresholdV.value()
        self.grabcut = self.grabcutV.value()
        self.radius = self.radiusV.value()
        print(self.confidence, self.threshold, self.grabcut, self.radius)
        message = QMessageBox()
        message.setWindowTitle("Input Received")
        message.setInformativeText("Testing Image {:s} with {:.2f} confidence level and {:.2f} threshold level".format(self.input,self.confidence,self.threshold))
        message.exec_()
        return (self.input, self.confidence, self.threshold, self.grabcut, self.radius)

def main():
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec_()

main()