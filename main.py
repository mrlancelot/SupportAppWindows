import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
import subprocess  # Import subprocess

class SystemTrayApp(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'System Tray App')
        self.menu = QMenu(parent)
        exitAction = self.menu.addAction("Quit")
        exitAction.triggered.connect(self.quit)
        self.setContextMenu(self.menu)
        self.activated.connect(self.on_click)

    def on_click(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            # Launch the app_gui.py script
            subprocess.Popen(['python', 'gui.py'])  # Ensure 'app_gui.py' is in the same directory or specify the full path

    def quit(self):
        QApplication.quit()

def main():
    app = QApplication(sys.argv)
    trayIcon = SystemTrayApp(QIcon("assets/frame0/key.png")) # Ensure you have an icon.png in your directory or change the path to a valid icon
    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



