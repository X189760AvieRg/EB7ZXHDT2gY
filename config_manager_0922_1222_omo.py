# 代码生成时间: 2025-09-22 12:22:17
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtGui import QTextCursor

"""
配置文件管理器
这个程序使用PyQt5框架创建一个简单的GUI应用程序，
用于加载、显示和保存配置文件。
"""

class ConfigManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和布局
        self.setWindowTitle('配置文件管理器')
        self.layout = QVBoxLayout()

        # 添加一个标签显示当前加载的文件路径
        self.filePathLabel = QLabel('当前文件路径：')
        self.layout.addWidget(self.filePathLabel)

        # 添加一个文本编辑器用于显示和编辑配置文件内容
        self.textEdit = QTextEdit()
        self.layout.addWidget(self.textEdit)

        # 添加一个按钮用于打开配置文件
        self.openButton = QPushButton('打开文件')
        self.openButton.clicked.connect(self.openFile)
        self.layout.addWidget(self.openButton)

        # 添加一个按钮用于保存配置文件
        self.saveButton = QPushButton('保存文件')
        self.saveButton.clicked.connect(self.saveFile)
        self.layout.addWidget(self.saveButton)

        # 布局添加到主窗口
        self.setLayout(self.layout)

    def openFile(self):
        # 打开文件对话框，让用户选择文件
        fileName, _ = QFileDialog.getOpenFileName(self, '打开文件', '/', '配置文件 (*.ini *.conf)')
        if fileName:
            self.loadFile(fileName)

    def loadFile(self, fileName):
        # 加载文件内容到文本编辑器
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                self.textEdit.setText(file.read())
                self.filePathLabel.setText('当前文件路径：' + fileName)
        except Exception as e:
            QMessageBox.critical(self, '错误', '加载文件失败：' + str(e))

    def saveFile(self):
        # 保存文本编辑器内容到文件
        try:
            with open(self.filePathLabel.text().split('：')[1].strip(), 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toPlainText())
            QMessageBox.information(self, '成功', '保存文件成功')
        except Exception as e:
            QMessageBox.critical(self, '错误', '保存文件失败：' + str(e))

    def run(self):
        self.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = ConfigManager()
    manager.run()