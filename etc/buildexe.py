import os

WINDOWS = "Windows"
LINUX = "Linux"
CLI = "CLI"
GUI = "GUI"

print("== Build Exe ==")

print("Windows or Linux")
userinput = input("Enter what OS to build for: ")

if userinput == WINDOWS or userinput == WINDOWS.lower():
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == CLI or selectExe == CLI.lower():
        os.system("powershell.exe -File .\\build\\build-cli\\windows\\windowscli.ps1")
    elif selectExe == GUI or selectExe == GUI.lower():
        os.system("powershell.exe -File .\\build\\build-gui\\windows\\windowsgui.ps1")
elif userinput == LINUX or userinput == LINUX.lower():
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == CLI or selectExe == CLI.lower():
        os.system("./build/build-cli/linux/linuxcli.sh")
    elif selectExe == GUI or selectExe == GUI.lower():
        os.system("./build/build-gui/linux/linuxgui.sh")
