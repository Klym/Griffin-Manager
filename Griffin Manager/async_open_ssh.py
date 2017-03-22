import asyncio
import subprocess

from config import server, mysql_host, ssh_host, ssh_user, ssh_pass

async def openSSHTunnel():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    putty_call_str = ["plink.exe", "-L", "%s:3306:%s:3306" % (server, mysql_host), "-pw", ssh_pass, "%s@%s" % (ssh_user, ssh_host)]
    process = await asyncio.create_subprocess_exec(*putty_call_str, stdout=asyncio.subprocess.PIPE, startupinfo=si)
    while True:
        line = await process.stdout.readline()
        if line:
            break
    return process