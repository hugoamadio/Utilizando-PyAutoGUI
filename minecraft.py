import pyautogui
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

#Inicio das Funções:

def diretorio():
    diretorio = str(filedialog.askopenfilename())
    print(diretorio)
    os.system(f"start {diretorio}")
    time.sleep(13)
    botaoEntrarnojogo()
    return diretorio


def botaoEntrarnojogo():
    while True:
        entrarnojogo = pyautogui.locateCenterOnScreen("entrarnojogo.png", confidence = 0.7)
        if entrarnojogo != None:
            print("Botão Entrar no jogo encontrado")
            time.sleep(1)
            pyautogui.click(entrarnojogo)
            botaoUmjogador()
            break
        else:
            time.sleep(1)
            print("Procurando o botão Entrar no Jogo")


def botaoUmjogador():
    while True:
        umjogador = pyautogui.locateCenterOnScreen("umjogador.png", confidence = 0.7)
        if umjogador != None:
            print("Botão Um Jogador encontrado")
            time.sleep(1)
            pyautogui.click(umjogador)
            botaoCriarumnovomundo()
            break
        else:
            time.sleep(1)
            print("Procurando o botão Um Jogador")


def botaoCriarumnovomundo():
    while True:
        criarumnovomundo = pyautogui.locateCenterOnScreen("criar um novo mundo.png", confidence = 0.9)
        if criarumnovomundo != None:
            print("Botao Criar um Novo Mundo encontrado")
            time.sleep(1)
            pyautogui.moveTo(criarumnovomundo)
            time.sleep(1)
            pyautogui.click(criarumnovomundo)
            alterarMododejogo()
            break
        else:
            time.sleep(1)
            print("Procurando o botão Criar um Novo Mundo")


def alterarMododejogo():
    while True:
        mododejogo = pyautogui.locateCenterOnScreen("mododejogo.png", confidence = 0.7)
        if mododejogo != None:
            print("Botão Modo de Jogo encontrado")
            time.sleep(1)
            pyautogui.click(mododejogo)
            time.sleep(1)
            pyautogui.click(mododejogo)
            criar()
            break
        else:
            time.sleep(1)
            print("Procurando o botão Modo de Jogo")



def criar():
    while True:
        time.sleep(1)
        botaoCriar = pyautogui.locateCenterOnScreen("criar.png")
        if botaoCriar != None:
            print("Botão criar encontrado")
            time.sleep(1)
            pyautogui.moveTo(botaoCriar)
            time.sleep(1)
            pyautogui.click(botaoCriar)
            time.sleep(1)
            fullscren()
            break
        else:
            time.sleep(1)
            print("Procurando o botão Criar")


def fullscren():
    time.sleep(4)
    pyautogui.press("f11")

# AQUI COMEÇA A INTERFACE
interface = Tk()
interface.title("Minecraft")
interface.config(background="white")
frm = ttk.Frame(interface, padding=10)
frm.grid()

# -----------------------------------------------------------------------------------------------------------------

ttk.Label(frm, font="Arial 14 bold", text="Minecraft").grid(column=2, row=0) # Texto "Automação Minecraft"
ttk.Button(frm, text="Quit", command=interface.destroy).grid(column=4, row=3)          # Botão Quit
label1 = ttk.Label(frm, text=" ").grid(column=3, row=1)                                # Label que carrega o diretório do arquivo
botaocorrigir = ttk.Button(frm, text="Corrigir").grid(column=3, row=3)

BotaoOk = ttk.Button(frm, text="Onde está o Minecraft?", command=diretorio).grid(column=2, row=3)     # Botão OK



# -----------------------------------------------------------------------------------------------------------------

interface.mainloop()