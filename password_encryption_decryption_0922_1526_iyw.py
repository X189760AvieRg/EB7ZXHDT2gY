# 代码生成时间: 2025-09-22 15:26:24
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import hashlib
import base64

# 密码加密解密类
class EncryptionDecryption(QThread):
    # 信号定义
    resultReady = pyqtSignal(str)
    progressValue = pyqtSignal(int)
    
    def __init__(self, password, mode):
        super().__init__()
        self.password = password
        self.mode = mode
    
    def run(self):
        # 根据模式进行加密或解密
        if self.mode == 'encrypt':
            result = self.encrypt(self.password)
        elif self.mode == 'decrypt':
            result = self.decrypt(self.password)
        else:
            raise ValueError('Invalid mode. Use 