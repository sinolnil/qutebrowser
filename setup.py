from sys import platform,argv
import os

# This module generate an updateConfig binary file to the specific OS(win/mac).


REPO = "https://raw.githubusercontent.com/sinolnil/qutebrowser/main/config.py"
WHOAMI = os.environ.get("USER") if os.environ.get("USER")!=None else os.environ.get("USERNAME")
fileName = "updateConfig"
win32Path = os.path.join('C:',os.sep,'Users',WHOAMI,'AppData','Roaming','qutebrowser','config')
macPath = ""

def darwinInstall():
    try:
        with open (fileName, "w+") as f:
            f.write(f"curl {REPO} -o ../config.py")
        os.chmod(f"./{fileName}",0o777)
        os.system(f"./{fileName}")
    except Exception as e:
        print(e)

def win32Install():
    file = os.path.join(win32Path,'userscripts')
    try:
        if not os.path.exists(file):
            print(f'Create {file}')
            os.makedirs(file)
    except Exception as e:
        print(e)
        
    file = os.path.join(file,fileName)
    import subprocess # for execute bat command
    try:
        with open ( file, "w+") as f:
            f.write(f"@echo on\n"
                    "echo 'Downloading script from github...'\n"
                    f"curl {REPO} -o {win32Path}/config.py --ssl-no-revoke")
    except Exception as e:
        print(e)
        
    print(f"PASS..Created win32Install at {file}")
    
    try:
        subprocess.run(file)
        print(f"PASS..Execute {fileName}")
    except Exception as e:
        print(f"FAIL..Something went wrong. [{e}]")


    
if platform == "linux" or platform == "linux2":
    print("[Detected Linux]")
    print("This should not be happen")
    pass

elif platform == "darwin": # OS X
    print("[Detected Mac OS]")
    darwinInstall()

elif platform == "win32": # Windows
    print("[Detected Windows OS]")
    fileName = fileName + '.bat'
    win32Install()

