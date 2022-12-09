from PyQt5 import QtWidgets
from searcher_window import SearchWindow

if __name__ == '__main__':
    
    app = QtWidgets.QApplication([])
    window = SearchWindow()
    window.show()
    app.exec()