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
from time import sleep

#print(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
#client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
#from_whatsapp_number = 'whatsapp:+14155238886'
#to_whatsapp_number = 'whatsapp:'+os.environ['MY_PHONE_NUMBER']
#print(from_whatsapp_number,to_whatsapp_number)
#message = client.messages.create(body='testelegal', from_=from_whatsapp_number, to=to_whatsapp_number)
#print(message.sid)
'''
Opening the browser and getting the ROM data
'''
browser = Firefox()
url = 'https://transferwise.com/br'
browser.get(url)
browser.implicitly_wait(5)

#Buton for select curency
firstButton = browser.find_element_by_xpath('//span/div/button/span')
firstButton.click()
browser.implicitly_wait(4)
#Selecting EUR currency
currencySelected = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span/div/ul/li[3]/a/span/span')
currencySelected.click()
browser.implicitly_wait(4)
#Selecting BRL currency
secondCurrencyButton = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/button/span[1]/i')
secondCurrencyButton.click()
browser.implicitly_wait(4)
#Calculating
secondCurrency = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/ul/li[12]/a/span/span')
secondCurrency.click()

browser.implicitly_wait(4)
sleep(4)

'''
Geting the value of the current currency
'''
priceTarget = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/input')
value = priceTarget.get_attribute('value')

intValue =int(value.split(',')[0].replace('.',''))
print(value, intValue)

#Todo: Implement the criteria for alert:
#Medium from last 3 days
#Derivative value of last hours
'''
Sending the information after criteria: Whatsapp
'''
if  intValue > 5000:
    #url_whatsapp = 'https://web.whatsapp.com/'
    #browser.get(url_whatsapp)
    #sleep(5)

    print('lavai')
    link_enviar_mensagem = 'https://api.whatsapp.com/send?phone=5584996331397&text='+str(intValue)
    browser.get(link_enviar_mensagem)
    print('pronto')

    #botao = browser.find_element_by_xpath('//*[@id="action-button"]')
    #botao.click()
    #sleep(4)

    #botao2 = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
    #botao2.click()
    #sleep(4)

    #Cleiton chat
    #busca = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    #busca.click()
    #busca.send_keys('cleiton')
    #browser.implicitly_wait(5)
    #cleitonporra =browser.find_element_by_xpath('//span[@title = "Cleiton"]')
    #entra_cleiton = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]/div[2]/div[1]')
    #entra_cleiton.click()
    #cleitonporra.click()
    #browser.implicitly_wait(5)
    #chat = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    #chat.click()
    #chat.send_keys('Teste! Enviado automaticamente. Preco do euro agora: '+value)
    #enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
    #enviar.click()

    #message = client.messages.create(body=value, from_=from_whatsapp_number, to=to_whatsapp_number)
    #print(message.sid)
    # remetente = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[1]/input')
    # remetente.send_keys('Thiago')
    # ddd = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[3]/input[2]')
    # ddd.send_keys('84')
    # phoneNumber = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[5]/input[1]')
    # phoneNumber.send_keys('996331397')
    # message= browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[4]/td/textarea')
    # message.send_keys(intValue)
    # buttonSend = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[6]/td/button')
    # browser.implicitly_wait(2)
    # buttonSend.click()

#browser.quit()
