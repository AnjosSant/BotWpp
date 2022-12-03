#PROGRAMA DE ENVIO AUTOMATICO DE MENSAGENS VIA WPP
#pip install selenium (version 4.7.2)
#pip install webdriver-manager (version 3.8.5)
#pip install tkhtmlview  (version 0.1.1)

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
from tkinter import *
from tkhtmlview import HTMLLabel

#Onde guardaremos as informações que vamos enviar
contatos = []
msg = []
imagens = []





#Função que valida o que está sendo enviado
def ValidarEnvio():
    if len(contatos) > 0 and (len(imagens) > 0 and (len(msg) > 0)):
        Enviar()
    else:
        print("err0")

    if len(contatos) != 0:

        if (len(msg) > 0 and (len(imagens) == 0)):
            EnviarMsg()
        elif (len(imagens) > 0 and (len(msg) == 0)):
            EnviarImg()
        else:
            messagebox.showwarning("Erro ao Enviar", "Preencha as informaçôes nescessárias")
    else:
        messagebox.showwarning(
        "Erro ao Enviar", "Preencha as informaçôes nescessárias")


#Função para Guardar o contato
def PegarContato():
    contato = inputContato.get()
    if contato != '':
        contatos.append(contato)
        print(contatos)
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso")
    else:
        messagebox.showwarning(
            "Erro ao enviar", "Digite o número ou nome do contato/Grupo")

#Função para apagar os contatos dentro do array
def ApagarContato():
    if len(contatos) > 0:
        contatos.clear()
        print(contatos)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Adicione pelo menos 1 contato")


#Função para Guardar a mensagem que vai ser enviada
def PegarMsg():  
    mensagem = inputMsg.get('1.0', 'end-1c')
    if mensagem != '':
        msg.append(mensagem)

        print(msg)
    else:
        messagebox.showwarning(
            "Erro ao enviar", "Digite uma mensagem")

#Função para apagar a mensagem
def ApagarMsg():
    if len(msg) > 0:
        msg.clear()
        print(msg)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Digite uma mensagem")


#Função para selecionar uma imagem
def PegarImg():
    enviando_img = filedialog.askopenfilename(initialdir='/', title="Select a File", filetypes=(
        ("Image files", ["jpg", "png", "jpeg"]), ("all files", "-")))
    if enviando_img != '':
        imagens.append(enviando_img)
        print(imagens)
    else:
        messagebox.showwarning(
            "Erro ao adicionar imagem", "Selecione uma imagem")

#Função para apaguar a imagem
def ApagarImg():
    if len(imagens) > 0:
        imagens.clear()
        print(imagens)
    else:
        messagebox.showwarning(
            "Erro ao apagar", "Adicione pelo menos 1 imagem")

#função para enviar caso exista uma imagem e uma mensagem
def Enviar():
   #Abre o whatsapp Web
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
   #Espera o QRcode ser Escaneado para prosseguir
    WebDriverWait(driver, timeout=9000000).until(
            EC.presence_of_element_located((By.ID, 'pane-side')))
    slp(1)

    #Procura o nome do contato ou grupo na barra de pesquisa
    def SearchContatos(contatos):
        caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
        caixa_pesquisa.send_keys(contatos, Keys.ENTER)
        slp(3)

    #DIGITAR A MENSAGEM E ENVIAR
    def SendMsg(msg):
        escrevendo_msg = driver.find_element(By.CLASS_NAME, "p3_M1")
        escrevendo_msg.send_keys(msg)
        slp(1.5)
        escrevendo_msg.send_keys("", Keys.ENTER)
        slp(1.5)

    #SELECIONAR A IMAGEM E ENVIAR
    def SendImg(imagens):
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(imagens)
        time.sleep(2)
        send = driver.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
        send.click()


    #REPETE O PROCESSO ATÉ SER FINALIZADO
    for contato in contatos:
        SearchContatos(contato)
        SendImg(imagens)
        SendMsg(msg)
        slp(1)


#FUNÇÃO QUE ENVIA SOMENTE A MENSAGEM
def EnviarMsg():
    # Abre o whatsapp Web
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    # Espera o QRcode ser Escaneado para prosseguir
    WebDriverWait(driver, timeout=9000000).until(
        EC.presence_of_element_located((By.ID, 'pane-side')))
    slp(1)

    # Procura o nome do contato ou grupo na barra de pesquisa
    def SearchContatos(contatos):
        caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
        caixa_pesquisa.send_keys(contatos, Keys.ENTER)
        slp(3)

    # DIGITAR A MENSAGEM E ENVIAR
    def SendMsg(msg):
        escrevendo_msg = driver.find_element(By.CLASS_NAME, "p3_M1")
        escrevendo_msg.send_keys(msg)
        slp(1.5)
        escrevendo_msg.send_keys("", Keys.ENTER)
        slp(1.5)


    # REPETE O PROCESSO ATÉ SER FINALIZADO
    for contato in contatos:
        SearchContatos(contato)
        SendMsg(msg)
        slp(1)


#FUNÇÃO QUE ENVIA SOMENTE A IMAGEM
def EnviarImg():
    # Abre o whatsapp Web
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    # Espera o QRcode ser Escaneado para prosseguir
    WebDriverWait(driver, timeout=9000000).until(
        EC.presence_of_element_located((By.ID, 'pane-side')))
    slp(1)

    # Procura o nome do contato ou grupo na barra de pesquisa
    def SearchContatos(contatos):
        caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
        caixa_pesquisa.send_keys(contatos, Keys.ENTER)
        slp(3)


    # SELECIONAR A IMAGEM E ENVIAR
    def SendImg(imagens):
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(imagens)
        time.sleep(2)
        send = driver.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
        send.click()

    # REPETE O PROCESSO ATÉ SER FINALIZADO
    for contato in contatos:
        SearchContatos(contato)
        SendImg(imagens)
        slp(1)

#INTERFACE
janela = Tk()

janela.title("ChatBOT")
janela.geometry("390x844")
janela.config(bg="#00A884")




textlabel = Label(
    janela, text="Digite o nome ou o número de um contato ou grupo").place(x=50, y=100, width=300)
inputContato = Entry(janela)
inputContato.place(x=50, y=150, width=180)
buttonContato = Button(janela, text="Adicionar Contato", command=PegarContato)
buttonContato.place(x=50, y=185)

removerContato = Button(janela, text="Apagar contatos", command=ApagarContato)
removerContato.place(x=250, y=185)


textlabelMsg = Label(
    janela, text="Digite a mensagem que vai ser enviada").place(x=50, y=220, width=300)
inputMsg = Text(janela)
inputMsg.place(x=50, y=280, width=300, height=200)
buttonMsg = Button(janela, text="Adicionar a mensagem", command=PegarMsg)
buttonMsg.place(x=50, y=500, width=150)

removerMsg = Button(janela, text="Apagar Mensagem", command=ApagarMsg)
removerMsg.place(x=230, y=500, width=130)

buttonImg = Button(janela, text="adionar imagem", command=PegarImg)
buttonImg.place(x=50, y=550, width=130)

removerImg = Button(janela, text="Apagar Imagens", command=ApagarImg)
removerImg.place(x=230, y=550, width=130)

buttonEnviar = Button(janela, text="Enviar", command=ValidarEnvio)
buttonEnviar.place(x=100, y=630, width=200,)
janela.mainloop()
