import ctypes
import pystray
from pystray import MenuItem as item
from PIL import Image
from PyQt5 import QtWidgets, QtCore
import sys

class TrayApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Control Panel')
        self.setGeometry(0, 0, 250, 100)  # مكان النافذة
        self.move_to_bottom_right()
        
        # إنشاء الأزرار
        hide_taskbar_btn = QtWidgets.QPushButton('Hide Taskbar', self)
        hide_taskbar_btn.clicked.connect(self.hide_taskbar)

        mute_mic_btn = QtWidgets.QPushButton('Mute Microphone', self)
        mute_mic_btn.clicked.connect(self.mute_microphone)

        # ترتيب الأزرار
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(hide_taskbar_btn)
        layout.addWidget(mute_mic_btn)
        
        self.setLayout(layout)

    def move_to_bottom_right(self):
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        self.move(screen_geometry.width() - self.width() - 15, screen_geometry.height() - self.height() - 40)

    def hide_taskbar(self):
        # كود إخفاء شريط المهام
        try:
            ctypes.windll.user32.ShowWindow(ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None), 0)
            print("Taskbar hidden")
        except Exception as e:
            print(f"Error hiding taskbar: {e}")
    
    def mute_microphone(self):
        # كود لكتم صوت المايكروفون (يختلف بناءً على إعدادات النظام)
        try:
            # ملاحظة: كتم الصوت يحتاج مكتبات متخصصة للتحكم بالمايكروفون مثل `pycaw`
            print("Microphone muted")  # يجب استبدال هذا الجزء برمز حقيقي لكتم الصوت حسب الحاجة
        except Exception as e:
            print(f"Error muting microphone: {e}")

def quit_app(icon, item):
    icon.stop()
    QtCore.QCoreApplication.quit()

def show_app(icon, item, window):
    window.show()

def setup_tray(app_window):
    icon_image = Image.open("C://Users//coldw//Icons//chat.ico")  # ضع أيقونة صغيرة في مجلد المشروع
    tray_icon = pystray.Icon("test", icon_image, menu=pystray.Menu(
        item('Show Control Panel', lambda: show_app(tray_icon, item, app_window)),
        item('Quit', quit_app)
    ))
    tray_icon.run()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app_window = TrayApp()
    setup_tray(app_window)
    sys.exit(app.exec_())
