from quamash import QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import asyncio
import Griffin_Manager as griffin

app = QApplication(sys.argv)
with QEventLoop(app) as loop:
    asyncio.set_event_loop(loop)
    window = QMainWindow()
    ui = griffin.MainForm(window)
    window.show()
    app.exec()
    loop.run_forever()
griffin.session.close()