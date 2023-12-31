import os

WINDOWS = "Windows"
LINUX = "Linux"
CLI = "CLI"
GUI = "GUI"

def build_windows(selected_exe):
    if selected_exe == CLI or selected_exe == CLI.lower():
        os.system("powershell.exe -File .\\build\\build-cli\\windows\\windowscli.ps1")
    elif selected_exe == GUI or selected_exe == GUI.lower():
        os.system("powershell.exe -File .\\build\\build-gui\\windows\\windowsgui.ps1")
    else:
        print("Invalid selection. Exiting...")

def build_linux(selected_exe):
    if selected_exe == CLI or selected_exe == CLI.lower():
        os.system("./build/build-cli/linux/linuxcli.sh")
    elif selected_exe == GUI or selected_exe == GUI.lower():
        os.system("./build/build-gui/linux/linuxgui.sh")
    else:
        print("Invalid selection. Exiting...")

print("== Build Exe ==")

print("Windows or Linux")
user_input = input("Enter what OS to build for: ")

if user_input.lower() == WINDOWS.lower():
    print("CLI or GUI")
    select_exe = input("Enter the Exe you want to build: ")
    build_windows(select_exe)
elif user_input.lower() == LINUX.lower():
    print("CLI or GUI")
    select_exe = input("Enter the Exe you want to build: ")
    build_linux(select_exe)
else:
    print("Invalid OS selection. Exiting...")

if user_input == WINDOWS or user_input == WINDOWS.lower():
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == CLI or selectExe == CLI.lower():
        os.system("powershell.exe -File .\\build\\build-cli\\windows\\windowscli.ps1")
    elif selectExe == GUI or selectExe == GUI.lower():
        os.system("powershell.exe -File .\\build\\build-gui\\windows\\windowsgui.ps1")
elif user_input == LINUX or user_input == LINUX.lower():
    print("CLI or GUI")
    selectExe = input("Enter the Exe you want to build: ")
    if selectExe == CLI or selectExe == CLI.lower():
        os.system("./build/build-cli/linux/linuxcli.sh")
    elif selectExe == GUI or selectExe == GUI.lower():
        os.system("./build/build-gui/linux/linuxgui.sh")
