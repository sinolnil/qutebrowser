from sys import platform,argv
import os

# This module generate an updateConfig binary file to the specific OS(win/mac).
# It will auto-delete after executing the commands.
fileName = "updateConfig"
whoami = os.environ.get("USER") if os.environ.get("USER")!=None else os.environ.get("USERNAME")
repo = "https://raw.githubusercontent.com/sinolnil/qutebrowser/main/config.py"


def darwinInstall():
    
    with open (fileName, "w+") as f:
        f.write(f"curl {repo} -o ../config.py")
    print("Created darwinInstall")
    os.chmod(f"./{fileName}",0o777)
    print(f"Change {fileName} permission")
    os.system(f"./{fileName}")
    print(f"Execute {fileName}")

def win32Install():
    
    with open (fileName + '.bat', "w+") as f:
        f.write(f"@echo on\n\
echo 'Downloading script from github...'\n\
curl {repo} -o C:\\Users\\{whoami}\\AppData\\Roaming\\qutebrowser\\config\\config.py --ssl-no-revoke")
    print("Created win32Install")

    
if platform == "linux" or platform == "linux2":
    pass

elif platform == "darwin": # OS X
    print("Detected Mac OS")
    darwinInstall()

elif platform == "win32": # Windows
    print("Detected Windows OS")
    win32Install()

os.remove(argv[0]) #self-delete
