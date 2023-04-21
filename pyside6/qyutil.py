#!/dev/null


import psutil
from PySide6 import QtCore


F_LOG = "/tmp/clash.log"
F_CACHE = "/tmp/clash/cache.db"
F_SAVED = "/home/darren/.clash/cache.db"


def running():

    for proc in psutil.process_iter():
        if "clash" in proc.name():
            print(proc)
            return True
    return False


def run():

    # achieved in clash_run
    # d = QtCore.QDir()
    # assert d.rename(F_CACHE, F_SAVED)
    p = QtCore.QProcess()
    p.setStandardOutputFile(F_LOG, mode=QtCore.QIODeviceBase.OpenModeFlag.Append)
    p.setProgram("/usr/local/bin/clash_run")
    p.setArguments(["dler"])
    assert p.startDetached()


def kill():

    QtCore.QFile.remove(F_SAVED)
    assert QtCore.QFile.copy(F_CACHE, F_SAVED)
    QtCore.QProcess().startDetached("/usr/bin/killall", arguments=["clash"])


def log():

    QtCore.QProcess().startDetached(
        "/usr/bin/alacritty", arguments=[
            "-t", "clash log",
            "-e", "/usr/bin/tail", "-c", "+0", "-f", F_LOG])
