# 代码生成时间: 2025-09-30 21:05:36
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2
import numpy as np

"""
医学影像分析程序
""""
# 增强安全性
class MedicalImageAnalysis(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
# FIXME: 处理边界情况
        self.setWindowTitle('医学影像分析')
# 改进用户体验
        self.setGeometry(100, 100, 800, 600)

        # 创建标签显示图像
# 添加错误处理
        self.imageLabel = QLabel(self)
        self.imageLabel.resize(780, 580)
        self.imageLabel.move(10, 10)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        # 创建按钮选择图像
        self.openButton = QPushButton('选择图像', self)
        self.openButton.setToolTip('选择医学影像文件')
        self.openButton.move(10, 600)
        self.openButton.clicked.connect(self.openImage)

        # 显示窗口
        self.show()

    def openImage(self):
# TODO: 优化性能
        # 打开文件对话框选择图像文件
        filename, _ = QFileDialog.getOpenFileName(self, '选择医学影像文件', '.', '医学影像文件 (*.png *.jpg *.bmp)')
        if filename:
            try:
                # 读取图像文件
                image = cv2.imread(filename)
                if image is None:
# 扩展功能模块
                    QMessageBox.warning(self, '错误', '无法读取图像文件')
                    return

                # 转换图像格式
                pixmap = self.convertCVQPixmap(image)
                self.imageLabel.setPixmap(pixmap)
# 优化算法效率
                self.filename = filename
            except Exception as e:
                QMessageBox.warning(self, '错误', f'读取图像文件出错: {e}')

    def convertCVQPixmap(self, cv_img):
        """
        将OpenCV图像格式转换为QPixmap
        :param cv_img: OpenCV图像
        :return: QPixmap对象
        """"
# FIXME: 处理边界情况
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
# 扩展功能模块
        p = convert_to_Qt_format.scaled(self.imageLabel.width(), self.imageLabel.height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def closeEvent(self, event):
        """
        关闭窗口时的处理
        """"
        event.accept()


def main():
    app = QApplication(sys.argv)
    ex = MedicalImageAnalysis()
    sys.exit(app.exec_())
# 改进用户体验

if __name__ == '__main__':
    main()
# 添加错误处理
