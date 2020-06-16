from selenium.webdriver import Firefox
import time

class ZapBot:
    def __init__(self):
        self.driver = Firefox()

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

class cotacao:

    def __init__(self):
        self.intValue = 0
        self.value = "0"


    def verCotacao(self, navegador):
        '''
        Opening the browser and getting the ROM data
        '''
        url = 'https://transferwise.com/br'
        navegador.get(url)
        time.sleep(5)

        #Buton for select curency
        firstButton = navegador.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span/div/button')
        firstButton.click()
        navegador.implicitly_wait(4)
        #Selecting EUR currency
        #<button class="btn btn-input btn-input-inverse btn-addon btn-lg dropdown-toggle" type="button" aria-expanded="false"><span><i class="currency-flag currency-flag-brl hidden-xs"></i>BRL</span><span class="caret"></span></button>
        currencySelected = navegador.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span/div/ul/li[3]/a/span/span')
        currencySelected.click()
        navegador.implicitly_wait(4)
        #Selecting BRL currency
        secondCurrencyButton = navegador.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/button/span[1]/i')
        secondCurrencyButton.click()
        navegador.implicitly_wait(4)
        #Calculating
        secondCurrency = navegador.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/ul/li[12]/a/span/span')
        secondCurrency.click()
        time.sleep(4)

        '''
        Geting the value of the current currency
        '''
        priceTarget = navegador.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/input')
        self.value = priceTarget.get_attribute('value')

        self.intValue =int(self.value.split(',')[0].replace('.',''))
        print (self.value, self.intValue)

    def analyseCotation(self, limit):
        #Todo: Implement the criteria for alert:
        #Medium from last 3 days
        #Derivative value of last hours
        '''
        Sending the information after criteria: Whatsapp
        '''
        if self.intValue > limit:
            self.mensagem = self.value
            return True

botzinho = ZapBot()
#botzinho.EnviaZap(botzinho.driver,"5000", "cleitonray", 'https://web.whatsapp.com/')

cotacao = cotacao()
cotacao.verCotacao(botzinho.driver)
if cotacao.analyseCotation(5740):
   botzinho.EnviaZap(botzinho.driver,"A cotacao atual do euro é: "+cotacao.value, "cleitonray", 'https://web.whatsapp.com/')
