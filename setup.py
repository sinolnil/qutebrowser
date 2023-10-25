from sys import platform
import os

# This module is to install the config-update command to qutebrwoser
fileName = "updateConfig"
repo = "https://raw.githubusercontent.com/sinolnil/qutebrowser/main/config.py"

def darwinInstall():
    with open (fileName, "w+") as f:
        f.write(f"curl {repo} -o ../config.py")
    print("darwinInstall download completed")
    os.chmod(f"./{fileName}",0o777)
    os.system(f"./{fileName}")

if platform == "linux" or platform == "linux2":
    pass

elif platform == "darwin": # OS X
    darwinInstall()

elif platform == "win32": # Windows
    pass

