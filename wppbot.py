from selenium import webdriver
from time import sleep as slp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#ACESSANDO O SITE
driver.get("https://web.whatsapp.com/")
#ESPERANDO ESQUENEAR O CÓDIGO
WebDriverWait(driver, timeout=30).until(EC.presence_of_element_located((By.ID, 'pane-side')))
slp(2)
#LISTA DE CONTATOS ONDE O BOT ENVIARA AS MSG
contatos = ["98725-3079", "94925-3432"]

#MENSAGEM QUE SERA ENVIADA


#TODO O PROCESSO DE PROCURAR O CONTATO E ENVIAR A MSG
for contato in contatos :
    #PESQUISANDO O CONTATO E ENTRANDO NA CONVERSA
    caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
    caixa_pesquisa.send_keys(contato, Keys.ENTER)
    slp(3)
    #ESCREVENDO A MENSAGEM PARA O CONTATO SELECIONADO
    escrevendo_msg= driver.find_element(By.CLASS_NAME, "p3_M1")
    escrevendo_msg.send_keys()
    #ENVIANDO A MENSAGEM DIGITADA
    slp(1.5)
    escrevendo_msg.send_keys("BOT N ESCREVI ISTO", Keys.ENTER)
    slp(1.5)

