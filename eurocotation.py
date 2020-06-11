from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
url = 'https://transferwise.com/br'
browser.get(url)
sleep(3)

#Buton for select curency
firstButton = browser.find_element_by_xpath('//span/div/button/span')
firstButton.click()
#Selecting EUR currency
currencySelected = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span/div/ul/li[3]/a/span/span')
currencySelected.click()
secondCurrencyButton = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/button/span[1]/i')
secondCurrencyButton.click()
secondCurrency = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/span/div/ul/li[12]/a/span/span')
secondCurrency.click()

sleep(1)
#firstButton.click()
'''
Geting the value of the current currency
'''
priceTarget = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/div[1]/div/div[2]/div/input')
value = priceTarget.get_attribute('value')

print(value)

intValue =int(value.split(',')[0].replace('.',''))

if  intValue > 5000:
    url = 'http://www.torpedogratuito.com/'
    browser.get(url)
    sleep(3)
    remetente = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[1]/input')
    remetente.send_keys('Thiago')
    ddd = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[3]/input[2]')
    ddd.send_keys('84')
    phoneNumber = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[2]/td[5]/input[1]')
    phoneNumber.send_keys('996331397')
    message= browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[4]/td/textarea')
    message.send_keys(intValue)
    buttonSend = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/table/tbody/tr[6]/td/button')
    sleep(2)
    buttonSend.click()

#browser.quit()
