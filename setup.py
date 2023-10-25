from sys import platform,argv
import os
# This module generate an updateConfig binary file to the specific OS(win/mac).
REPO = "https://raw.githubusercontent.com/sinolnil/qutebrowser/main/config.py"
WHOAMI = os.environ.get("USER") if os.environ.get("USER")!=None else os.environ.get("USERNAME")
fileName = "updateConfig"
win32Path = os.path.join('C:',os.sep,'Users',WHOAMI,'AppData','Roaming','qutebrowser','config')
macPath = ""


def writeFile(path,fileName,script,mode="w+"):
    print(f"Paht:{path} FileName:{fileName}")
    print("Writing file...")
    try:
        with open(path + '/' + fileName,mode) as f:
            f.write(script)
    except Exception as e:
        print(e)
def darwinInstall():
    try:
        with open (fileName, "w+") as f:
            f.write(f"curl {REPO} -o ../config.py")
        os.chmod(f"./{fileName}",0o777)
        os.system(f"./{fileName}")
    except Exception as e:
        print(e)

def win32Install():
	path = os.path.join(win32Path,'userscripts')
	try:
		if not os.path.exists(path):
			print(f'Create {path}')
			os.makedirs(path)
	except Exception as e:
		print(e)
	updateConfig = (f"@echo on\n"
				"echo 'Downloading script from github...'\n"
				f"curl {REPO} -o {win32Path}/config.py --ssl-no-revoke")

	openConfig = (f"@echo on\n"
               "start C:/Users/%USERNAME%/AppData/Roaming/qutebrowser/config")

	writeFile(path,fileName,updateConfig)
	writeFile(path,'openConfig.bat',openConfig)

	try:
		import subprocess # for execute bat command
		subprocess.run(os.path.join(path,fileName))
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
