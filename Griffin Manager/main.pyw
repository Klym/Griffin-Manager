from quamash import QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import sys
import asyncio
import subprocess
import Griffin_Manager as griffin

def eventExitHandler():
    griffin.session.close()
    if griffin.ssh_process is not None:
        griffin.ssh_process.terminate()
    loop.close()

app = QApplication(sys.argv)
app.aboutToQuit.connect(eventExitHandler)
with QEventLoop(app) as loop:
    asyncio.set_event_loop(loop)
    window = QMainWindow()
    try:
        ui = griffin.MainForm(window)
        window.show()
        loop.run_forever()
    except Exception as ex:
        msgBox = QMessageBox()
        exit = msgBox.about(window, "Ошибка", ex.args[0])
        sys.exit(exit)
    sys.exit(app.exec())