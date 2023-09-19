import os

print("== Build Exe ==")

print("Windows or Linux")
userinput = input("Enter what OS to build for: ")

if userinput == "Windows":
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == "CLI":
        os.system("powershell.exe -File .\\build\\build-cli\\windows\\windowscli.ps1")
    elif selectExe == "GUI":
        os.system("powershell.exe -File .\\build\\build-gui\\windows\\windowsgui.ps1")
elif userinput == "Linux":
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == "CLI":
        os.system("./build/build-cli/linux/linuxcli.sh")
    elif selectExe == "GUI":
        os.system("./build/build-gui/linux/linuxgui.sh")
