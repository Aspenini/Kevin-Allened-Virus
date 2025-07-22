import sys, random, pygame, threading
from PyQt5 import QtWidgets, QtGui, QtCore

# === FILES ===
KEVIN_IMAGE = "kevin_allen.png"
KEVIN_AUDIO_NORMAL = "kevin_theme_compressed.mp3"
KEVIN_AUDIO_SUPERSONIC = "kevin_supersonic_with_alarm.mp3"  # <-- your custom alarm-mix goes here

# === TIMINGS & SETTINGS ===
INITIAL_KEVINS = 5
SPAWN_INTERVAL = 5000
POPUP_INTERVAL = 6000
FLASH_INTERVAL = 100
ACTIVATION_TIME = 5000  # in ms

POPUP_MESSAGES = [
    "Kevin.exe is watching...",
    "System32 is being deleted...",
    "Your system is now haunted.",
    "You just got Kevin Allened.",
    "There is no escape.",
    "Critical vibes detected.",
    "Why did you run this?"
]

HIDE_FLAGS = QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint

# === Kevin Sprite ===
class KevinWindow(QtWidgets.QWidget):
    def __init__(self, fast=False):
        super().__init__()
        self.setWindowFlags(HIDE_FLAGS)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pixmap = QtGui.QPixmap(KEVIN_IMAGE)
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())

        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        self.screen_width = screen.width()
        self.screen_height = screen.height()

        self.x = random.randint(0, self.screen_width - self.width())
        self.y = random.randint(0, self.screen_height - self.height())
        speed = random.uniform(6, 10) if not fast else random.uniform(18, 30)
        self.vx = random.choice([-1, 1]) * speed
        self.vy = random.choice([-1, 1]) * speed

        self.move(int(self.x), int(self.y))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(16)

    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0 or self.x + self.width() >= self.screen_width:
            self.vx *= -1
        if self.y <= 0 or self.y + self.height() >= self.screen_height:
            self.vy *= -1
        self.move(int(self.x), int(self.y))


# === Flashing Color Overlay + Deletion Bar ===
class FlashOverlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(HIDE_FLAGS | QtCore.Qt.X11BypassWindowManagerHint)
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.color_timer = QtCore.QTimer()
        self.color_timer.timeout.connect(self.flash)
        self.color_timer.start(FLASH_INTERVAL)

        self.progress = 0
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(100, 100, 800, 40)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("Deleting System32... %p%")
        self.setStyleSheet("QProgressBar { font-size: 18px; }")
        self.bg_color = QtGui.QColor(255, 0, 0, 100)

        self.progress_timer = QtCore.QTimer()
        self.progress_timer.timeout.connect(self.update_bar)
        self.progress_timer.start(200)

    def flash(self):
        r = random.randint(100, 255)
        g = random.randint(0, 255)
        b = random.randint(100, 255)
        self.bg_color = QtGui.QColor(r, g, b, 200)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), self.bg_color)
        self.setPalette(palette)

    def update_bar(self):
        self.progress = min(100, self.progress + random.randint(1, 5))
        self.progress_bar.setValue(self.progress)


# === Popup Box ===
class KevinPopup(QtWidgets.QMessageBox):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Windows Info")
        self.setText(message)
        self.setIcon(QtWidgets.QMessageBox.Information)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.setWindowFlags(HIDE_FLAGS)
        QtCore.QTimer.singleShot(2000, self.accept)


# === The App ===
class KevinApp(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.kevins = []
        self.overlay = None
        self.hell_mode = False

        threading.Thread(target=self.play_music, args=(KEVIN_AUDIO_NORMAL,), daemon=True).start()
        for _ in range(INITIAL_KEVINS):
            self.spawn_kevin()

        self.spawn_timer = QtCore.QTimer()
        self.spawn_timer.timeout.connect(self.spawn_kevin)
        self.spawn_timer.start(SPAWN_INTERVAL)

        self.popup_timer = QtCore.QTimer()
        self.popup_timer.timeout.connect(self.spawn_popup)
        self.popup_timer.start(POPUP_INTERVAL)

        QtCore.QTimer.singleShot(ACTIVATION_TIME, self.activate_hell_mode)

    def spawn_kevin(self):
        k = KevinWindow(fast=self.hell_mode)
        k.show()
        self.kevins.append(k)

    def spawn_popup(self):
        msg = random.choice(POPUP_MESSAGES)
        popup = KevinPopup(msg)
        popup.show()

    def play_music(self, track):
        pygame.mixer.init()
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)

    def activate_hell_mode(self):
        self.hell_mode = True
        self.overlay = FlashOverlay()
        self.overlay.show()

        pygame.mixer.music.stop()
        threading.Thread(target=self.play_music, args=(KEVIN_AUDIO_SUPERSONIC,), daemon=True).start()

        for k in self.kevins:
            k.vx *= 2.5
            k.vy *= 2.5


if __name__ == "__main__":
    app = KevinApp(sys.argv)
    sys.exit(app.exec_())
