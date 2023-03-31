import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Create the executable.
setup(
    name="Calculator App",
    version="1.0",
    description="A simple calculator app",
    options={"build_exe": build_exe_options},
    executables=[Executable("calculator.py", base=base)]
)
