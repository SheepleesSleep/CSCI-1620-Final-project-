from controller import*
from PyQt5.Qt import QApplication

def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()

if __name__ =='__main__' :
    main()