# login_window.py

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
from PySide6.QtGui import QPixmap  # 确保已经导入 QPixmap

from PySide6.QtCore import Signal

# import paramiko
# from CoreWin import CoreWin
from PySide6.QtCore import Qt


class LoginWindow(QWidget):
    # # 新添加的信号
    # open_second_window_signal = Signal(
    #     str, str, str, paramiko.SSHClient
    # )  # 修改信号参数类型

    def __init__(self):
        super().__init__()

        # 添加成员变量以保存 CoreWin 对象
        self.core_win = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("登录")
        self.setFixedSize(1920, 1080)

        # 创建一个 QLabel 用于背景图片
        background_label = QLabel(self)
        background_label.setFixedSize(1920, 1080)
        pixmap = QPixmap("beijing.jpg")
        background_label.setPixmap(
            pixmap.scaled(1920, 1080, Qt.KeepAspectRatioByExpanding)
        )

        # 创建组件
        ip_label = QLabel("IP地址:")
        username_label = QLabel("用户名:")
        password_label = QLabel("密码:")
        # self.ip_input = QLineEdit('101.101.100.100')
        # self.username_input = QLineEdit('root')
        # self.password_input = QLineEdit('1')

        self.ip_input = QLineEdit("172.30.194.77")
        self.username_input = QLineEdit("thebs")
        self.password_input = QLineEdit("er2wqar")

        self.password_input.setEchoMode(QLineEdit.Password)  # 隐藏密码

        # self.ip_input = QLineEdit('192.168.1.1')  # 设置默认IP地址
        # self.username_input = QLineEdit('your_username')  # 设置默认用户名
        # self.password_input = QLineEdit('your_password')  # 设置默认密码

        connect_button = QPushButton("连接")
        connect_button.clicked.connect(self.connect_ssh)  # 连接按钮点击时触发连接函数

        # 设置控件的样式
        self.setStyleSheet("""
            QLineEdit, QPushButton {
                width: 200px;  /* 控制宽度 */
                height: 30px;  /* 控制高度 */
                font-size: 16px; 
                margin: 10px 0;
            }
            QPushButton {
                height: 40px;
            }
        """)

        # 创建布局
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(ip_label, 0, Qt.AlignCenter)
        layout.addWidget(self.ip_input, 0, Qt.AlignCenter)
        layout.addWidget(username_label, 0, Qt.AlignCenter)
        layout.addWidget(self.username_input, 0, Qt.AlignCenter)
        layout.addWidget(password_label, 0, Qt.AlignCenter)
        layout.addWidget(self.password_input, 0, Qt.AlignCenter)
        layout.addWidget(connect_button, 0, Qt.AlignCenter)
        layout.addStretch()

        # 设置窗口布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle("登录界面")
        self.setGeometry(300, 300, 300, 200)

    def connect_ssh(self):
        ip_address = self.ip_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        # 检查是否为特定的用户名、密码和IP
        if ip_address == "1" and username == "1" and password == "1":
            # 创建或显示 CoreWin
            if not self.core_win:
                self.core_win = CoreWin(ip_address, username, password)
                self.core_win.show()
            else:
                self.core_win.show()
        else:  # 进行SSH连接
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip_address, username=username, password=password)

                # 如果 CoreWin 对象不存在，则创建一个
                if not self.core_win:
                    self.core_win = CoreWin(ip_address, username, password, ssh)
                    self.core_win.show()
                else:
                    # 如果 CoreWin 对象已存在，则显示它
                    self.core_win.show()

            except Exception as e:
                # 连接失败，显示错误信息弹窗
                error_message = f"连接失败: {str(e)}"
                QMessageBox.critical(self, "错误", error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
