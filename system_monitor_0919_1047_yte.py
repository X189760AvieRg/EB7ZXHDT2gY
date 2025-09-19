# 代码生成时间: 2025-09-19 10:47:54
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import QTimer
"""
系统性能监控工具
使用Python和PyQt框架实现
"""

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('系统性能监控工具')
# TODO: 优化性能
        self.setGeometry(100, 100, 400, 300)

        # 创建布局
# 增强安全性
        layout = QGridLayout()

        # 创建标签显示CPU使用率
        self.cpuLabel = QLabel('CPU使用率: 0%')
        layout.addWidget(self.cpuLabel, 0, 0)

        # 创建标签显示内存使用情况
        self.memLabel = QLabel('内存使用情况: 0%')
        layout.addWidget(self.memLabel, 0, 1)

        # 创建按钮，用于刷新数据
        self.refreshButton = QPushButton('刷新')
        self.refreshButton.clicked.connect(self.refreshData)
        layout.addWidget(self.refreshButton, 1, 0, 1, 2)
# FIXME: 处理边界情况

        # 设置布局
        self.setLayout(layout)

        # 初始化定时器，定时刷新数据
        self.timer = QTimer(self.updateData)
        self.timer.start(1000) # 1秒刷新一次

    def updateData(self):
        """更新系统性能数据"""
        try:
            # 获取CPU使用率
            cpu_usage = psutil.cpu_percent(interval=1)
            self.cpuLabel.setText(f'CPU使用率: {cpu_usage}%')

            # 获取内存使用率
# 添加错误处理
            mem = psutil.virtual_memory()
            mem_usage = mem.percent
            self.memLabel.setText(f'内存使用情况: {mem_usage}%')
# NOTE: 重要实现细节
        except Exception as e:
            print(f'更新数据时发生错误: {e}')

    def refreshData(self):
        """手动刷新数据"""
        self.updateData()

def main():
    # 创建应用
    app = QApplication(sys.argv)
    # 创建系统监控窗口
    monitor = SystemMonitor()
    # 显示窗口
    monitor.show()
    # 进入应用主循环
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()