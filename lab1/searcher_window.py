from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic
from db_connection import get_database
from PyQt5.Qt import QDesktopServices, QUrl, QApplication, QColor, Qt
from PyQt5.QtWidgets import QTextEdit

from Help import Help
#from calculations import get_files_list, get_folders_content, eq_rating, sort_key
from searcher_ops import get_rated_files

from PyQt5 import QtCore, QtGui, QtWidgets

class MyWidget(QtWidgets.QTextEdit):

    def mousePressEvent(self, e):
        self.anchor = self.anchorAt(e.pos())

    def mouseReleaseEvent(self, e):
        if self.anchor:
            QDesktopServices.openUrl(QUrl(self.anchor))
            self.anchor = None
        
class SearchWindow(QMainWindow):
    def init_search_res(self):
        self.resultInfo= MyWidget(self.centralwidget)
        self.resultInfo.setGeometry(QtCore.QRect(10, 130, 811, 421))
        self.resultInfo.setReadOnly(True)
        self.resultInfo.setObjectName("textEdit_result")
            
        self.resultInfo.show() 
    
    
    def showSearchResults(self, results):
        self.resultInfo.clear()
        
        for result in results:
            #print(result[0])
            cursor = self.resultInfo.textCursor()
            fmt = cursor.charFormat()
            fmt.setForeground(QColor('blue'))
            address = result[0]
            fmt.setAnchor(True)
            fmt.setAnchorHref(address)
            fmt.setToolTip(address)
            cursor.insertText(f"{result[0]} - {result[1]}\n", fmt) 
    
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        #self.folder_path = ''
        #self.file_path = ''
        #self.search_string = ''
        
        
        #db_connection = ''
        
        dbname = get_database()
        self.collection = dbname['files']
        
        #self.b_file = False
        #self.b_dir = False
        self.actionhelp.triggered.connect(self.help_clicked)
        #self.btn_directory_dialog.clicked.connect(self.openDirectoryDialog)
        self.init_search_res()

    def btn_search_clicked(self):
        search_str = self.textEdit_search.toPlainText()
        
        database_files = list(self.collection.find({}))
        
        #files = get_files_list(get_folders_content(self.folder_path))
        #files = files + database_files
            
        #eq_rating(files, search_str)
            
        results = [[file['path'], ','.join(file['words_from_query']), file['eq_rate']] for file in get_rated_files(database_files, search_str) if file['eq_rate'] > 0]
            
        #self.textEdit_result.clear()
        self.showSearchResults(results)
        #for file in result:
        #    print(file[0])
        #    cursor = self.textEdit_result.textCursor()
        #    fmt = cursor.charFormat()
        #    fmt.setForeground(QColor('blue'))
        #    address = file[0]
            
        #    fmt.setAnchor(True)
        #    fmt.setAnchorHref(address)
        #    fmt.setToolTip(address)
        #    cursor.insertText(f"{file[0]} - {file[1]}\n", fmt)    
        #    fmt.setForeground(QColor('black'))

    def help_clicked(self):
        dial = Help(self)
        dial.show()
        
    #def openDirectoryDialog(self):
    #    pass
        #self.b_file = False
        #self.b_dir = True
        #self.folder_path = QFileDialog.getExistingDirectory(self)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = SearchWindow()
    window.show()
    app.exec()
