import asyncio
import subprocess

from quamash import QThreadExecutor
from config import server, mysql_host, ssh_host, ssh_user, ssh_pass

async def run_process():
    with QThreadExecutor(1) as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, openSSHTunnel)

def openSSHTunnel():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    putty_call_str = ["plink.exe", "-L", "%s:3306:%s:3306" % (server, mysql_host), "-pw", ssh_pass, "%s@%s" % (ssh_user, ssh_host)]
    process = subprocess.Popen(putty_call_str, stdout=subprocess.PIPE, startupinfo=si)
    while True:
        line = process.stdout.readline()
        if line:
            break
    return process