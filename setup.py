import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'


executables = [cx_Freeze.Executable('main.py',base=base ,icon='icon.ico')]

cx_Freeze.setup(
    name = 'Visioniyam',
    options = {"build_exe":{"packages":["mediapipe","os","PySide6","pyautogui","math","cv2"] , "include_files":["icon.ico","logo.png"]}},
    version = "1.00",
    description = 'This app helps you control mouse with your iris.',
    executables = executables
)