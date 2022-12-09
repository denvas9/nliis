import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QLabel
from PyQt5 import QtCore


class Example(QDialog):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        for i in range(4):
            for j in range(2):
                if not i and not j:
                    self.tableWidget.setCellWidget(
                        i, j, 
                        QLabel('''
                            <a href="d:/EYAZIS/ILang1/texta/this.txt"> 
                                Как вставить гиперссылку в QTableWidget? 
                            </a>''',
                            openExternalLinks=True)
                    )
                else:
                    item = QTableWidgetItem("Item {}-{}".format(i, j))
                    item.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.tableWidget.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())