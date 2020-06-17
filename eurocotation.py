##################################################
## Currency analisys software with whatsapp alerts
##################################################
## no license
##################################################
## Author: {Thiago}
## Credits: [{Thiago}]
## License: {no}
## Version: {1}.{0}.{0}
## Email: {thiago_liveira@hotmail.com}
## Status: {in_progress}
##################################################

#Imports
from selenium.webdriver import Firefox
import time
import numpy
from bot import ZapBot

class browser:
    def __init__(self):
        self.browser = Firefox()

class Cotacao:

    def __init__(self):
        self.intValue = 0
        self.value = "0"

    def readCotation(self):
        f = open("cotacao.txt", "r")
        return f.read()

    def writeCotation(self, cotation):
        f = open("cotacao.txt", "a")
        f.write(str(cotation)+",")
        f.close()

    def verCotacao(self, navegador):
        '''
        Opening the browser and getting the ROM data
        '''
        url = 'https://transferwise.com/br'
        navegador.get(url)
        time.sleep(5)
        '''
        Selecting the currency
        '''
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
        #print (self.value, self.intValue)

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

def main():
    zapBot = ZapBot()
    cotacao = Cotacao()
    contact = "eunatal"
    timeAnalysis = 280
    while True:
        cotacoes = cotacao.readCotation()
        my_numbers = [int(n) for n in cotacoes[:-1].split(",")]
        media = numpy.mean(my_numbers)
        cotacao.verCotacao(zapBot.browser)
        cotacao.writeCotation(cotacao.intValue)
        print("Atual: " + str(cotacao.value), "Media: " + str(media))
        if cotacao.analyseCotation(media):
           zapBot.EnviaZap(zapBot.browser,"A cotacao atual do euro é: " + cotacao.value, contact, 'https://web.whatsapp.com/')
        time.sleep(15)
        zapBot.browser.back()
        time.sleep(timeAnalysis)

    zapBot.browser.quit()

if __name__ == '__main__':
    main()
