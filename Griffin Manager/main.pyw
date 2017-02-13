from quamash import QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import asyncio
import Griffin_Manager as griffin

def eventExitHandler():
    griffin.session.close()
    loop.close()

app = QApplication(sys.argv)
app.aboutToQuit.connect(eventExitHandler)
with QEventLoop(app) as loop:
    asyncio.set_event_loop(loop)
    window = QMainWindow()
    ui = griffin.MainForm(window)
    window.show()
    sys.exit(app.exec())