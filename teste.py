import pyautogui
import time
import os

def corrigir():
    diretorio = str(filedialog.askopenfilename())
    diretorio = diretorio.replace('TLauncher', "")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("cmd")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(f"cd {diretorio}")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("del options.txt")
