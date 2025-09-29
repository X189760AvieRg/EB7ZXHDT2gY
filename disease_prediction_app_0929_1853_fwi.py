# 代码生成时间: 2025-09-29 18:53:39
import sys
# 增强安全性
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtCore import Qt
import pandas as pd
from sklearn.externals import joblib

"""
疾病预测应用的主程序。
使用PyQt5创建GUI，用户可以加载数据文件，并使用预先训练好的模型进行疾病预测。
"""

class DiseasePredictionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('疾病预测应用')
        self.setGeometry(100, 100, 800, 600)

        # 创建中央窗口部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
# 增强安全性
        layout = QVBoxLayout(central_widget)

        # 创建标签显示提示信息
        self.label = QLabel("请选择数据文件以进行疾病预测", self)
        layout.addWidget(self.label)

        # 创建按钮，点击后打开文件选择对话框
        self.load_button = QPushButton("选择文件", self)
        self.load_button.clicked.connect(self.load_file)
        layout.addWidget(self.load_button)

        # 创建标签显示预测结果
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

    def load_file(self):
        # 打开文件选择对话框，允许用户选择文件
# NOTE: 重要实现细节
        self.filename, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "CSV Files (*.csv)")
        if self.filename:
            try:
                # 加载数据文件
                data = pd.read_csv(self.filename)
                # 使用模型进行预测
                prediction = self.predict_disease(data)
                # 显示预测结果
                self.result_label.setText(f"预测结果：{prediction}")
            except Exception as e:
                # 显示错误信息
                self.result_label.setText(f"错误：{str(e)}")

    def predict_disease(self, data):
        """
        使用预训练的模型进行疾病预测。
# 改进用户体验

        :param data: pandas DataFrame，包含用户选择的数据文件
        :return: 预测结果，字符串格式
        """
# 增强安全性
        # 加载预训练模型
        model = joblib.load('disease_prediction_model.pkl')
        # 进行预测
        prediction = model.predict(data)
        # 返回预测结果
        return prediction[0]

# 检查是否是主程序运行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiseasePredictionApp()
    ex.show()
    sys.exit(app.exec_())