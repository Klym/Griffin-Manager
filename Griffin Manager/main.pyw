from quamash import QEventLoop
from sqlalchemy.exc import OperationalError
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from config import server, mysql_host, ssh_host, ssh_user, ssh_pass

import sys
import asyncio
import subprocess
import Griffin_Manager as griffin

def openSSHTunnel():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    putty_call_str = ["plink.exe", "-L", "%s:3306:%s:3306" % (server, mysql_host), "-pw", ssh_pass, "%s@%s" % (ssh_user, ssh_host)]
    process = subprocess.Popen(putty_call_str, stdout=subprocess.PIPE, startupinfo=si)
    while True:
        line = process.stdout.readline()
        if process.poll() is not None:
            break
        if line:
            print(line.strip().decode('cp866'))
            break
    return process

def eventExitHandler():
    griffin.session.close()
    ssh_process.terminate()
    loop.close()

app = QApplication(sys.argv)
app.aboutToQuit.connect(eventExitHandler)
ssh_process = openSSHTunnel()
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