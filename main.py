from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys

top = 400
left = 400
width = 800
height = 600
f = open('text.txt', 'w')

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        title = "Приложенька рисовалка"

        icon = "cat.jpg"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setFixedSize(width,height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.Fig = 'pen'

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.white
        self.lastPoint = QPoint()
        self.countFig = 0

        self.label = QLabel(self)
        self.label.setFixedSize(500, 500)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Файл")
        brushSize = mainMenu.addMenu("Размер кисти")
        brushColor = mainMenu.addMenu("Цвет")
        brushFig = mainMenu.addMenu("Фигура")

        loadAction = QAction("Загрузить", self)
        fileMenu.addAction(loadAction)
        loadAction.triggered.connect(self.loadFile)

        saveAction = QAction("Сохранить",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction("Очистить", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        exitAction = QAction("Выход", self)
        fileMenu.addAction(exitAction)
        exitAction.triggered.connect(qApp.quit)

        threepxAction = QAction("3px", self)
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePixel)

        fivepxAction = QAction("5px", self)
        brushSize.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePixel)

        sevenpxAction = QAction("7px", self)
        brushSize.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPixel)

        ninepxAction = QAction("9px", self)
        brushSize.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePixel)

        blackAction = QAction("Черный", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)


        whitekAction = QAction("Белый", self)
        brushColor.addAction(whitekAction)
        whitekAction.triggered.connect(self.whiteColor)


        redAction = QAction("Красный", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction("Зеленый", self)
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction("Желтый", self)
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        penAction = QAction("Карандаш", self)
        brushFig.addAction(penAction)
        penAction.triggered.connect(self.penPaint)

        recAction = QAction("Квадрат", self)
        brushFig.addAction(recAction)
        recAction.triggered.connect(self.recPaint)

        cirAction = QAction("Круг", self)
        brushFig.addAction(cirAction)
        cirAction.triggered.connect(self.circlePaint)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            self.firstPoint = event.pos()
            self.countFig += 1
            f.write("Фигура " + str(self.countFig) + " : ( " + str(self.lastPoint.x()) + " ; " + str(self.lastPoint.y()) + " ) \n")

    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            if self.Fig == 'pen':
                painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            if self.Fig == 'circle':
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawEllipse(self.lastPoint, 10, 10)


    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )

    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.image = QImage(filename[0]).scaled(width, height, Qt.IgnoreAspectRatio)

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)


    def clear(self):
        self.image.fill(Qt.black)
        self.update()

    def recPaint(self):
        self.Fig = 'rectangle'

    def circlePaint(self):
        self.Fig = 'circle'

    def penPaint(self):
        self.Fig = 'pen'

    def threePixel(self):
        self.brushSize = 3

    def fivePixel(self):
        self.brushSize = 5

    def sevenPixel(self):
        self.brushSize = 7

    def ninePixel(self):
        self.brushSize = 9


    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()