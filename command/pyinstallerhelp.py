import os
import sys

command = "pyinstaller -h"
try:
    # os.system(command)
    with open("pyinstallerhelp.txt",'a') as f:
        print(os.system(command), file=f)
except Exception as e:
    print(e)