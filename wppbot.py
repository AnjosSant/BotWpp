from selenium import webdriver
from time import sleep as slp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from webbrowser import get
from tkinter import filedialog
from tkinter import messagebox
import time
import tkinter.font as tkFont

contatos = []
msg = []
imagens = []


def PegarContato():
    contato = inputContato.get()
    if contato != '':
        contatos.append(contato)
        print(contatos)
    else:
        messagebox.showwarning(
            "Erro ao enviar", "Digite o número ou nome do contato/Grupo")


def ApagarContato():
    if len(contatos) > 0:
        contatos.clear()
        print(contatos)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Adicione pelo menos 1 contato")


def PegarMsg():  
    mensagem = inputMsg.get('1.0', 'end-1c')
    if mensagem != '':
        msg.append(mensagem)
        print(msg)
    else:
        messagebox.showwarning(
            "Erro ao enviar", "Digite uma mensagem")


def ApagarMsg():
    if len(msg) > 0:
        msg.clear()
        print(msg)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Digite uma mensagem")


def PegarImg():
    enviando_img = filedialog.askopenfilename(initialdir='/', title="Select a File", filetypes=(
        ("Image files", ["*jpg*", "*png*", "*jpeg*"]), ("all files", "*-*")))
    imagens.append(enviando_img)
    if enviando_img != '':
        imagens.append(enviando_img)
        print(imagens)
    else:
        messagebox.showwarning(
            "Erro ao adicionar imagem", "Selecione uma imagem")


def ApagarImg():
    if len(imagens) > 0:
        imagens.clear()
        print(imagens)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Adicione pelo menos 1 imagem")


def Enviar():
    if len(contatos) > 0 and (len(imagens) > 0 or (len(msg) > 0)):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    WebDriverWait(driver, timeout=9000000).until(
        EC.presence_of_element_located((By.ID, 'pane-side')))
    slp(1)


    def SearchContatos(contatos):
        caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
        caixa_pesquisa.send_keys(contatos, Keys.ENTER)
        slp(3)

    def SendMsg(msg):
        escrevendo_msg = driver.find_element(By.CLASS_NAME, "p3_M1")
        escrevendo_msg.send_keys(msg)
        slp(1.5)
        escrevendo_msg.send_keys("", Keys.ENTER)
        slp(1.5)

    def SendImg(imagens):
       
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()     
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(imagens)
        time.sleep(2)
        send = driver.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
        send.click()    
        
        
    for contato in contatos:
        SearchContatos(contato)
        SendMsg(msg)
        SendImg(imagens)
    else:
        messagebox.showerror(
            "Erro ao enviar", "Preencha as informações corretamente...")


janela = Tk()

janela.title("ChatBOT")
janela.geometry("800x600")

textlabel = Label(
    janela, text="Digite o nome ou o número de um contato ou grupo").place(x=50, y=100)
inputContato = Entry(janela)
inputContato.place(x=50, y=200)
buttonContato = Button(janela, text="10 e faixa", command=PegarContato)
buttonContato.place(x=100, y=300)

removerContato = Button(janela, text="Apagar contatos", command=ApagarContato)
removerContato.place(x=100, y=320)

inputMsg = Text(janela)
inputMsg.place(x=100, y=350, width=300, height=450)
buttonMsg = Button(janela, text="Adicionar a mensagem", command=PegarMsg)
buttonMsg.place(x=100, y=400)

removerMsg = Button(janela, text="Apagar Mensagem", command=ApagarMsg)
removerMsg.place(x=100, y=420)

buttonImg = Button(janela, text="adionar imagem", command=PegarImg)
buttonImg.place(x=100, y=450)
buttonEnviar = Button(janela, text="Enviar", command=Enviar)
buttonEnviar.place(x=100, y=480)

removerImg = Button(janela, text="Apagar Imagens", command=ApagarImg)
removerImg.place(x=100, y=500)

janela.mainloop()
