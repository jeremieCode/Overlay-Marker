from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QObject, QRect
from PyQt5.QtGui import QPainter, QColor, QPen
import sys
from pynput import mouse
from pynput.mouse import Button
import keyboard


class SignalEmitter(QObject):
    circle_added = pyqtSignal(int, int)
    circles_cleared = pyqtSignal()
    toggle_layer = pyqtSignal()
    app_quit = pyqtSignal()


class TransparentOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.on_top = True
        self.signals = SignalEmitter()
        self.signals.circle_added.connect(self.add_circle)
        self.signals.circles_cleared.connect(self.clear_circles)
        self.signals.toggle_layer.connect(self.toggle_on_top)
        self.signals.app_quit.connect(QApplication.instance().quit)

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.showFullScreen()

        self.start_listeners()

        print("Calque démarré AU PREMIER PLAN")
        print("F9 = Toggle premier plan / arrière plan")
        print("Clic droit = Ajouter cercle")
        print("Espace = Effacer cercles")
        print("Échap = Quitter")
    
    def start_listeners(self):
        def on_click(x, y, button, pressed):
            if button == Button.right and pressed and self.on_top:
                self.signals.circle_added.emit(x, y)
            return True
        
        self.mouse_listener = mouse.Listener(on_click=on_click)
        self.mouse_listener.daemon = True
        self.mouse_listener.start()
        
        def on_f9():
            self.signals.toggle_layer.emit()
        
        def on_space():
            if self.on_top:
                self.signals.circles_cleared.emit()
                return True
            return False
        
        def on_esc():
            self.signals.app_quit.emit()
        
        keyboard.on_press_key('f9', lambda _: on_f9())
        keyboard.on_press_key('space', lambda _: on_space(), suppress=True)
        keyboard.on_press_key('esc', lambda _: on_esc())
    
    def toggle_on_top(self):
        self.on_top = not self.on_top
        if self.on_top:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            self.show()
            self.raise_()
            self.activateWindow()
            print("=> Calque AU PREMIER PLAN (vous pouvez marquer les points)")
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            self.show()
            self.lower()
            print("=> Calque EN ARRIÈRE PLAN (vous pouvez jouer)")
        self.update()
    
    def add_circle(self, x, y):
        self.circles.append(QPoint(x, y))
        print(f"Cercle ajouté à ({x}, {y}). Total: {len(self.circles)}")
        self.update()
    
    def clear_circles(self):
        count = len(self.circles)
        self.circles.clear()
        print(f"{count} cercle(s) effacé(s)")
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if len(self.circles) == 0:
            if self.on_top:
                overlay_color = QColor(100, 100, 255, 15)
            else:
                overlay_color = QColor(255, 100, 100, 10)
            painter.fillRect(self.rect(), overlay_color)
        
        for index, pos in enumerate(self.circles, start=1):
            color = QColor(255, 255, 0, 200)
            painter.setBrush(color)
            
            pen = QPen(QColor(255, 165, 0, 255))
            pen.setWidth(4)
            painter.setPen(pen)
            
            radius = 25
            painter.drawEllipse(pos, radius, radius)
            
            pen = QPen(QColor(0, 0, 0, 255))
            painter.setPen(pen)
            font = painter.font()
            font.setPixelSize(16)
            font.setBold(True)
            painter.setFont(font)
            
            text_rect = QRect(pos.x() - radius, pos.y() - radius, radius * 2, radius * 2)
            painter.drawText(text_rect, Qt.AlignCenter, str(index))
    
    def closeEvent(self, event):
        if hasattr(self, 'mouse_listener'):
            self.mouse_listener.stop()
        keyboard.unhook_all()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = TransparentOverlay()
    sys.exit(app.exec_())
