from selenium.webdriver import Firefox
import time

class ZapBot:
    def __init__(self):
        self.browser = Firefox()

    def EnviaZap(self,navegador,message, contato, website='https://web.whatsapp.com/'):
        #Definindo website
        navegador.get(website)
        time.sleep(15)
        busca = navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        busca.click()
        busca.send_keys(contato)
        time.sleep(4)
        conversa = navegador.find_element_by_xpath(f'//span[@title="{contato}"]')
        time.sleep(3)
        conversa.click()
        #Elemento da caixa de texto         <div tabindex="-1" class="_3uMse">
        texto = navegador.find_element_by_xpath("//div[contains(@class, '_3FRCZ')][contains(@data-tab, '1')]")
        time.sleep(3)
        texto.click()
        texto.send_keys(message)
        time.sleep(3)
        #Elemento do botão enviar           <span data-icon="send" class="">
        enviar = navegador.find_element_by_xpath("//button[@class='_1U1xa']")
        time.sleep(2)
        enviar.click()
