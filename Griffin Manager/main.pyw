from quamash import QEventLoop
from sqlalchemy.exc import OperationalError
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

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
    try:
        ui = griffin.MainForm(window)
        window.show()
    except OperationalError as ex:
        msgBox = QMessageBox()
        exit = msgBox.about(window, "Ошибка соединения с базой данных", "Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение")
        sys.exit(exit)
    except Exception as ex:
        msgBox = QMessageBox()
        exit = msgBox.about(window, "Ошибка", ex.args[0])
        sys.exit(exit)
    sys.exit(app.exec())