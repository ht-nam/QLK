from cx_Freeze import Executable, setup

setup(
    name="QLK",
    version="1.0.1",
    description="UserVer",
    executables=[Executable("main.py", base="Win32GUI")],
)
