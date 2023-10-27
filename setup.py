from sys import platform,argv
import os
# This module generate an updateConfig binary file to the specific OS(win/mac).
REPO = "https://raw.githubusercontent.com/sinolnil/qutebrowser/main/config.py"
WHOAMI = os.environ.get("USER") if os.environ.get("USER")!=None else os.environ.get("USERNAME")
win32Path = os.path.join('C:',os.sep,'Users',WHOAMI,'AppData','Roaming','qutebrowser','config')
macPath = f"/Users/{WHOAMI}/.qutebrowser"


def writeFile(path,fileName,script,mode="w+"):
    try:
        if not os.path.exists(path):
            print(f"Create {path}")
            os.makedirs(path)
        else:
            print("File found")
    except Exception as e:
        print(f"Exception [writeFile] {e}")


    try:
        with open(os.path.join(path,fileName),mode) as f:
            print(f"Writing file...@ {path} file:{fileName}")
            f.write(script)
    except Exception as e:
        print(e)

def darwinInstall():
    path = os.path.join(macPath,'userscripts')
    updateConfig = (f"curl {REPO} -o ../config.py")
    writeFile(path,'updateConfig',updateConfig)

    #execute updateConfig
    try:
        #change the permission
        f = "updateConfig"
        os.chmod(f"./{f}",0o777)
        os.system(f"./{f}") 
    except Exception as e:
        print(e)

def win32Install():
	path = os.path.join(win32Path,'userscripts')
	updateConfig = (f"@echo on\n"
				f"curl {REPO} -o {win32Path}/config.py --ssl-no-revoke")

	openConfig = (f"@echo on\n"
               "start C:/Users/%USERNAME%/AppData/Roaming/qutebrowser/config")

	writeFile(path,"updateConfig.bat",updateConfig)
	writeFile(path,"openConfig.bat",openConfig)

	try:
		import subprocess # for execute bat command
		subprocess.run(os.path.join(path,'updateConfig.bat'))
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
    win32Install()

