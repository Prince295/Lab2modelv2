import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QPushButton, QRadioButton, QWidget, QHBoxLayout, \
    QLCDNumber, QApplication, QSlider, QLabel, QAbstractButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example( QWidget ):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setStyleSheet( "QRadioButton {font: 14pt Comic Sans MS}" )
        self.cb1 = QRadioButton( 'Состояние 1', self )
        grid.addWidget( self.cb1, 0, 0 )

        self.cb2 = QRadioButton( 'Состояние 2', self )
        grid.addWidget( self.cb2, 1, 0 )

        self.cb3 = QRadioButton( 'Состояние 3', self )
        grid.addWidget( self.cb3, 2, 0 )

        self.cb4 = QRadioButton( 'Состояние 4', self )
        grid.addWidget( self.cb4, 3, 0 )

        self.cb5 = QRadioButton( 'Состояние 5', self )
        grid.addWidget( self.cb5, 4, 0 )

        self.cb6 = QRadioButton( 'Состояние 6', self )
        grid.addWidget( self.cb6, 5, 0 )

        self.cb7 = QRadioButton( 'Состояние 7', self )
        grid.addWidget( self.cb7, 6, 0 )

        self.btn1 = QPushButton( "Запустить", self )
        self.btn1.setStyleSheet( "font: 16pt Comic Sans MS" )

        self.sliderLabel = QLabel( "Количество тактов", self )
        self.sliderLabel.setStyleSheet( "QLabel {font: 20pt Comic Sans MS}" )
        self.sliderLabel.setAlignment( Qt.AlignCenter )
        self.lcd = QLCDNumber( self )
        self.sld = QSlider( Qt.Horizontal, self )
        self.OutLabel = QLabel( self )
        self.OutLabel.setStyleSheet("font: 20pt Comic Sans MS; background-color: #808080; border: 2px solid #3873d9;")
        self.OutLabel.setText( "           Текущий выход         =         ")

        self.btn1.clicked.connect( self.auto )
        grid.addWidget( self.sliderLabel, 0, 2, 2, 2 )
        grid.addWidget( self.lcd, 2, 2, 2, 2 )
        grid.addWidget( self.sld, 4, 2, 1, 2 )
        grid.addWidget( self.btn1, 6, 3 )
        grid.addWidget( self.OutLabel, 7, 0, 1, 4 )
        self.setLayout( grid )
        self.sld.valueChanged.connect( self.lcd.display )
        self.setFocusPolicy( Qt.NoFocus )

        self.setGeometry( 300, 300, 550, 380 )
        self.setWindowTitle( 'Автономный автомат' )
        self.show()

    def auto(self):
        if self.cb1.isChecked() == True:
            x=1
        if self.cb2.isChecked() == True:
            x=2
        if self.cb3.isChecked() == True:
            x=3
        if self.cb4.isChecked() == True:
            x=4
        if self.cb5.isChecked() == True:
            x=5
        if self.cb6.isChecked() == True:
            x=6
        if self.cb7.isChecked() == True:
            x=7
        y = 1
        takt = self.sld.value()
        out = [[6, 1], [4, 2], [7, 3], [3, 2], [1, 1], [2, 1], [5, 3]]
        for i in range( takt ):
            y = out[x - 1][1]
            x = out[x - 1][0]
        self.OutLabel.setText( "           Текущий выход         =         " + str( y )  )
        return y


if __name__ == '__main__':
    app = QApplication( sys.argv )
    ex = Example()
    sys.exit( app.exec_() )


